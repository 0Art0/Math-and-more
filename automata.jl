using Base.Iterators
using Pipe

###Finite Automata

abstract type FA end  #Data type for finite automata

#Deterministic Finite Automata
struct DFA{T} <: FA  #T indicates the type of the state
    Σ :: Array  #alphabet of the automaton
    Q :: Array  #the set of states of the automaton
    δ :: Array{Array{T}}   #the transition function of the automaton
    q₀ #the start state, q₀ ∈ Q
    F :: Array #the set of final states F ⊆ Q
end

const NFA = DFA{Array}  #Non-deterministic finite automata

const ϵ_NFA = DFA{Array}  #Non-finite automaton with ϵ-transitions
const ϵ = "" #the empty string

#an actual transition "function", instead of a table
δ(A::DFA, state, α) = try A.δ[findfirst(isequal(state), A.Q)][findfirst(isequal(α), A.Σ)]; catch missing end

ϵ_closure(A::ϵ_NFA, states) = states == [] ? [] : [union!([ϵ_closure(A, δ(A, state, ϵ)) for state in states]...); states]

#δ^, the extended transition function for parsing strings in Σ⃰
𝛅(A::DFA, state, input::Tuple) = input == () || state == missing ? state : 𝛅(A, δ(A, state, input[1]), input[2:end])
𝛅(A::NFA, states, input::Tuple) = input == () || states == [] ? states : 𝛅(A, union([δ(A, state, input[1]) for state in states]...), input[2:end])
𝛅ₑ(A::ϵ_NFA, states, input::Tuple) = input == () || states == [] ? states : 𝛅ₑ(A, union([δ(A, state, input[1]) for state in ϵ_closure(A, states)]...), input[2:end])

#checks whether a given string is in the language of a DFA
inL(A::DFA, input::Tuple)::Bool = 𝛅(A, A.q₀, input) in A.F
inL(A::NFA, input::Tuple)::Bool = length(intersect(𝛅(A, [A.q₀], input), A.F)) > 0
inLₑ(A::ϵ_NFA, input::Tuple)::Bool = length(intersect(ϵ_closure(A, 𝛅ₑ(A, [A.q₀], input)), A.F)) > 0

#generates the set of all strings in the language Σ
Σₙ(A::Vector, n::Int64)::Vector{NTuple} = product(repeated(A, n)...) |> collect |> vec
Σ⃰(A::Vector, n::Int64)::Vector{Tuple{Vararg{T, N} where N} where T} = vcat([Σₙ(A, k) for k = 0:n]...)

#Subset construction to convert an NFA to a DFA
subsets(a::Array)::Array{Array} = [[e for (i, e) in enumerate(a) if (bitstring(b)[end+1-i] == '1')] for b = 0:2^length(a) - 1]
subsetconstruction(A::NFA)::DFA = DFA{Array}(A.Σ, subsets(A.Q), [[sort!(union([δ(A, state, α) for state in s])) for α in A.Σ] for s in subsets(A.Q) if s != []], [A.q₀], [s for s in subsets(A.Q) if length(intersect(s, A.F)) > 0])

un_ϵ(A::ϵ_NFA)::NFA = NFA(A.Σ[1:end-1], A.Q, [[𝛅(A, ϵ_closure(A, [state]), (α, )) for α in A.Σ if α != ϵ] for state in A.Q], A.q₀, [state for state in A.Q if length(intersect(ϵ_closure(A, [state]), A.F)) > 0])

###Specific DFAs

modchecker = (n::Int64 -> DFA{Int64}([0, 1], 0:n-1, [[(2*s) % n, (2*s + 1) % n] for s = 0:n-1], 0, [0]))

check3 = modchecker(3)

checkerboard = NFA(["r", "b"], 1:9, [ [[2, 4], [5]], [[4, 6], [1, 3, 5]], [[2, 6], [5]], [[2, 8], [1, 5, 7]], [[2, 4, 6, 8], [1, 3, 7, 9]], [[2, 8], [3, 5, 9]], [[4, 8], [5]], [[4, 6], [5, 7, 9]], [[6, 8], [5]] ], 1, [9])

[word for word in Σ⃰(checkerboard.Σ, 6) if inL(checkerboard, word)] .|> join |> println

repeat3remover = DFA{String}([0, 1, 2], ["START", "0A", "0B", "1A", "1B", "2A", "2B", "DEAD"], [
["0A", "1A", "2A"],
["0B", "1A", "2A"],
["DEAD", "1A", "2A"],
["0A", "1B", "2A"],
["0A", "DEAD", "2A"],
["0A", "1A", "2B"],
["0A", "1A", "DEAD"],
["DEAD", "DEAD", "DEAD"]],
"START", ["0A", "0B", "1A", "1B", "2A", "2B"])

Σ⃰(repeat3remover.Σ, 5)

###Regular expressions

const αₗ = String  #type for the individual characters/alphabets of a language
const Σₗ = Vector{αₗ}   #type for the alphabet of a language
const Regₗ = Vector{αₗ}     #type for regular langauges

const ϵₗ = ""::αₗ   #the empty string
const ∅ₗ = αₗ[]::Regₗ   #the empty language

↢(RL::Regₗ, A::Σₗ)::Bool = @pipe RL |> *(_...) |> split(_, "") |> union |> (_ ⊆ A)

⊕(RLₐ::Regₗ, RLᵦ::Regₗ)::Regₗ = [RLₐ .* β for β in RLᵦ] |> (a -> reduce(vcat, a))
import Base.∪; ∪(RLₐ::Regₗ, RLᵦ::Regₗ)::Regₗ = RLₐ ∪ RLᵦ
✳(RL::Regₗ, n=10) = Σ⃰(RL, n)

#removes leading and trailing whitespaces from a string
trim(s::String) = s[1] == ' ' ? trim(s[2:end]) : (s[end] == ' ' ? trim(s[1:end-1]) : s)
parseRegₗ(regₗ::String)::Regₗ = (split(regₗ, r" |\[|\]|,", keepempty = false) .* "")

#parses a regular expression and returns a tree
function parseregex(regex::String)
    #trim the string to remove whitespaces
    regex = trim(regex)
    #remove external parentheses
    if regex[firstindex(regex)] == '(' && regex[lastindex(regex)] == ')'
        rex = (ex -> ex[nextind(ex, firstindex(ex)):prevind(ex, lastindex(ex))])(regex)
        regex = ([c == '(' ? 1 : (c == ')' ? -1 : 0) for c in rex] |> (a -> Iterators.accumulate(+, a)) |> collect .>= 0) |> (a -> reduce(&, a)) ? rex : regex
    end
    #check for infix operators - ⊕ and ∪
    b = 0
    for ind in eachindex(regex)
        c = regex[ind]; b += (c == '(' ? 1 : (c == ')' ? -1 : 0))
        b == 0 && (c == '⊕' || c == '∪') ? (return (parseregex(regex[1:prevind(regex, ind)]), parseregex(regex[nextind(regex, ind):end]), c == '⊕' ? "concat" : "union")) : continue
    end
    #check if the string is of the form ✳(<expr>)
    regex[1] == '✳' ? (return (parseregex(regex[nextind(regex, 1):end]), "kleene")) : nothing
    #check if the string is of the form [<α>] - terminates recursion
    regex[1] == '[' && regex[end] == ']' ? (return (parseRegₗ(regex), "Rₗ")) : nothing
end

###Examples of Regular Expressions

ex = "(✳([a]) ∪ ([b] ⊕ [c])) ⊕ ✳([d] ∪ [e])"

A12 = ϵ_NFA(['1', '2', ϵ], ['0', '1', '2', '3', '4', '5'], [
[[], [], ['2', '4']],
[[], [], []],
[['3'], [], []],
[[], [], ['1']],
[[], ['5'], []],
[[], [], ['1']],
], '0', ['1'])

(ex |> parseregex)

un_ϵ(A12)

function generatϵNFA(regex, n = 0)::ϵ_NFA
    etype = regex[end]
    if etype == "Rₗ"

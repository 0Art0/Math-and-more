using Base.Iterators
###Code for regular languages

#generates the list of all possible strings of a given size in a given language
Σₙ(A::Vector, n::Int64)::Vector{NTuple} = product(repeated(A, n)...) |> collect |> vec
Σ⃰(A::Vector, n::Int64)::Vector{Tuple{Vararg{T, N} where N} where T} = vcat([Σₙ(A, k) for k = 0:n]...)

const αₗ = String  #type for the individual characters/alphabets of a language
const Σₗ = Vector{αₗ}   #type for the alphabet of a language
const Regₗ = Vector{αₗ}     #type for regular langauges

const ϵₗ = ""::αₗ   #the empty string
const ∅ₗ = αₗ[]::Regₗ   #the empty language

#checks whether a given regular language is drawn from a given alphabet
↢(RL::Regₗ, A::Σₗ)::Bool = @pipe RL |> *(_...) |> split(_, "") |> union |> (_ ⊆ A)

#concatenation of languages
⊕(RLₐ::Regₗ, RLᵦ::Regₗ)::Regₗ = [RLₐ .* β for β in RLᵦ] |> (a -> reduce(vcat, a))
#union of languages
import Base.∪; ∪(RLₐ::Regₗ, RLᵦ::Regₗ)::Regₗ = RLₐ ∪ RLᵦ
#Kleene star of a langauge
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

###An example

ex = "(✳([a]) ∪ ([b] ⊕ [c])) ⊕ ✳([d] ∪ [e])"

ex |> parseregex

###

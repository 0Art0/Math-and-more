#using Pipe

#Permutation groups, implemented in Julia

const Permutation = Array{Int64, 1}  #the "Permutation" data type, which is implemented as a linear array of numbersusing

#generates the set of permutations of n objects
function Sₙ(n::Int64)::Vector{Permutation}
    permutations::Vector{Permutation} = [[]]

    for i in 1:n
        permutations = [[p; m] for p in permutations for m in 1:n if !(m in p)]
    end
    permutations
end

#generate a subgroup of Sₙ with an element i fixed
#Hᵢ(n::Int64, i::Int64) = begin; sw = ®([[i, n]], n); [sw ⊚ ®(©(σ), n) ⊚ sw for σ in Sₙ(n-1)]; end ::Vector{Permutation}
Hᵢ(n::Int64, i::Int64)::Vector{Permutation} = filter((σ::Permutation -> σ[i] == i), Sₙ(n))

#converts a permutation into a function
(⋋)(σ::Permutation)::Function = (i -> σ[i])

#the identity permutation in Sₙ
eₙ(n::Int64)::Permutation = (1:n)

#composition of permutations
(⊚)(σ::Permutation, τ::Permutation)::Permutation = (τ |> (σ |> ⋋))

#inverse of a permutation
(≀)(σ::Permutation)::Permutation = indexin(1:length(σ), σ)

#power of a permutation
function (⋏)(σ::Permutation, n::Int64)::Permutation
    n > 0 ? σ ⊚ (⋏(σ, (n-1))) : (n == 0 ? eₙ(length(σ)) : ⋏(≀(σ), -n))
end

#a general function ♻ that generates the cyclic group of ◧ by repeated application of some function f
♻(◧::Array, f::Function)::Array = ◧[end] |> f |> (□ -> (□ == ◧[1] ? ◧ : ♻(push!(◧, □), f)))

#calculates the "order" of a permutation in Sₙ
order(σ::Permutation)::Int64 = (♻([σ], (τ::Vector{Int64} -> (σ ⊚ τ)::Vector{Int64})) |> length)

#decomposes a permutation into cycles
function ©(σ::Permutation, ⦰::Bool = false)::Vector{Vector{Int64}}
    🚲::Vector{Vector{Int64}} = []

    for u in 1:length(σ)
        u in vcat(🚲...) ? nothing : push!( 🚲, ♻([u], ⋋(σ)) )
    end
    !⦰ ? 🚲 : filter((x::Vector{Int64} -> length(x) > 1), 🚲)
end

#converts the cyclic form of a permutation into the regular list representation
function ®(🚲::Vector{Vector{Int64}}, n = -1)::Permutation
    🚴 =  eₙ(n < 0 ? length(vcat(🚲...)) : n)
    for ⚪ in 🚲
        for (i, e) in enumerate(⚪)
           🚴[e] = ⚪[mod(i+1, 1:length(⚪))]
        end
    end
    🚴
end

#orthogonal matrix permutation
A(σ::Permutation)::BitArray{2} = BitArray(i == σ[j] for i = 1:length(σ), j = 1:length(σ))

#inverse orthogonal matrix permutation (converts back to standard form)
A⁼(Σ::Array{Int64, 2})::Permutation = Σ * eₙ(ndims(Σ))

#the sign of a permutation
sgn(σ::Permutation)::Int64 = (-1)^mod(length(σ) - length(©(σ)), 2)

#conjugates a permutation with another permutation s
conjugate(σ::Permutation, s::Permutation)::Permutation = s ⊚ σ ⊚ ≀(s)

#assigns a unique number to a permutation
function factoradical(σ::Permutation)::Int64
    n = length(σ)

    s = σ[1]
    n == 1 ? 0 : (s-1)*factorial(n-1) + (σ[2:end] |> (τ -> replace(τ, Dict(zip(sort(τ), 1:n-1))...)) |> factoradical)

    #s = σ[end]
    #n == 1 ? 0 : (s-1)*factorial(n-1) + @pipe (σ |> ®([[n, s]], n) ⊚ _ |> ©(_, true) |> ®(_, n-1) |> factoradical)
end

#the conjugacy classes of Sₙ
function 𝒪(n::Int64, display=false)
    tree, s, O = trues(factorial(n)), Sₙ(n), Vector{Vector{Vector{Int64}}}[]

    for (pos, perm) in enumerate(s)
        class = Vector{Vector{Int64}}[]; branch = Int64[]
        if tree[pos]
            for mutation in s
                c = ≀(mutation) ⊚ perm ⊚ (mutation); f = factoradical(c) + 1
                f in branch ? nothing : push!(class, ©(c, true))
                push!(branch, f); tree[f] = false
            end
            push!(O, class)
        end
    end

    if display
        for (num, class) in enumerate(O)
            println("\n\nClass $num \n")
            for e in class
                print("[ ")
                    for cycle in e
                        print(Tuple(cycle), " ")
                    end
                print("]\t")
            end
        end
    end
    O
end

#the centre of Sₙ
#Z(n::Int64) = (s -> @pipe(BitArray(conjugate(p, m) == p for p in s, m in s) |> mapslices(prod, _, dims=1) |> s .* (BitArray(_)') |> filter((σ -> sum(σ) != 0), _)))(Sₙ(n))
Z(n::Int64) = filter((a::Array -> length(a) == 1), 𝒪(n)) |> (list -> reduce(vcat, list))

#returns the cycle type of a permutation
cycletype(σ::Permutation)::Vector{Int64} = ©(σ) .|> length |> sort |> reverse

#returns the number of partitions of n with atmost m parts
partitions(n::Int64, m::Int64)::Int64 = (m == 0 || n < 0) ? 0 : ((n == 0 || m == 1) ? 1 : partitions(n-m, m) + partitions(n, m-1))
partitions(n::Int64)::Int64 = partitions(n, n)

#returns the Cartesian product of all the sets in the list
function cartesianproduct(lists)
    x = [[]]

    for list in lists
        x = [push!(copy(a), elem) for elem in list for a in x]
    end
    x
end

partitions(6)

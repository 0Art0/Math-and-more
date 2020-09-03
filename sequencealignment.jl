# a function to generate all possible choices of r elements out of n choices
# the details of its implementation can be ignored
function combinations(n::Int64, r::Int64)
    choices = [ntuple(i -> false, n)]

    tail(v::NTuple) = length(v) == 0 ? 0 : v[end] ? length(v) : tail(v[1:end-1])
    insert(v::NTuple, pos::Int64) = ntuple(i -> i != pos ? v[i] : true, length(v))

    for k = r:-1:1
        new_choices = NTuple{n, Bool}[]
        for c in choices
            append!(new_choices, [insert(c, i) for i = 1+tail(c):n-(k-1)])
        end
        choices = deepcopy(new_choices)
    end

    choices
end

# a function to create a potential alignment between sequences A and B, based on a "choice"
#the choice is a Boolean vector of length m+n, containing m `trues` and n `falses`
function align(choice, A::String, B::String)::String #A is assumed to be longer than B
    α, β = choice[1:length(A)], choice[length(A)+1:end]

    k, ins = 0, [B[j] for (j, b) in enumerate(β) if b]

    [a ? '-' : begin k += 1; ins[k] end for (i, a) in enumerate(α)] |> String
end

# assigns a score to the alignment
function score(aligned::String, A::String, B::String)::Float64
    ∇ = length(filter(c -> c != '-', aligned))

     sum([(c == A[i]) ? 1 : 0 for (i, c) in enumerate(aligned)]) - ( (length(A) - ∇) + (length(B) - ∇) )
end

# the final process of choosing the best alignment
function finalign(seqA::String, seqB::String) #seqA is longer than seqB
    max_score, best_align = 0.0, seqA

    for seq_align in align.(combinations(length(seqA) + length(seqB), length(seqA)), seqA, seqB)
        if score(seq_align, seqA, seqB) > max_score
            max_score, best_align = score(seq_align, seqA, seqB), seq_align
        end
    end
    (max_score, best_align)
end

finalign("ATTGCTA", "ATGCCA")

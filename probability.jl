using Plots
using Combinatorics

theme(:juno)

struct ProbabilitySpace{N<:Number}
    Ω::Vector{N}
    𝓕::Vector{Vector{N}}
    𝙿::Dict{N, Float64}
end

P(S::ProbabilitySpace{N}, x::N) where N <: Number = S.𝙿[x]

𝓟(S::ProbabilitySpace{N}, e::Vector{N}) where N <: Number = [P(S, x) for x in e] |> sum

𝔼(S::ProbabilitySpace, f = (x::Number -> x)) = [P(S, ω)*f(ω) for ω in S.Ω] |> sum

plotPDF(D::Dict{N, Float64}) where N <: Number = plot(D, seriestype = :bar, ylims = (0, 1), title = "Probability distribution function", ylabel = "Probability", xlabel = "Values", leg = false)
plotPDF(S::ProbabilitySpace) = plotPDF(S.𝙿)

function sample(S::ProbabilitySpace)
    r = rand()
    for ω in S.Ω
        r -= S.𝙿[ω]

        if r < 0
            return ω
        end
    end
end

function simulate(R, n_trials::Int64 = 10000)
    outcomes = Dict{Number, Float64}()
    for _ in 1:n_trials
        r = R(0)
        outcomes[r] = (r in keys(outcomes) ? outcomes[r] : 0) + 1
    end

    for k in keys(outcomes)
        outcomes[k] /= n_trials
    end

    return outcomes
end

simulate(S::ProbabilitySpace) = simulate((_ -> sample(S)))

function CentralLimitTheorem(S::ProbabilitySpace, n::Int64, n_trials = 10000)
    R = (_ -> ([sample(S) for _ in 1:n] |> sum)/n)

    dist = simulate(R, n_trials)

    print(dist |> collect |> sort)

    plotPDF(dist)
end

###

UniformRandomVariable(𝛺::Vector{N}) where N <: Number = ProbabilitySpace{typeof(𝛺[end])}(𝛺, collect(powerset(𝛺)), Dict([(𝜔, 1/length(𝛺)) for 𝜔 in 𝛺]))

Bernoulli(p::Float64) = ProbabilitySpace{Int64}([0, 1], collect(powerset([0, 1])), Dict([(1, p), (0, 1 - p)]))

B = Bernoulli(0.9)

CentralLimitTheorem(B, 300)

#Future plan: Define sums and products of random variables

p = 7   #prime

function order(a::Int64, b::Int64)::Int64 #returns the smallest `m` such that aᵐ ≡ 1 (mod b)
    m, α = 0, 1
    while α != 1 || m == 0
        α = mod(α * a, b); m += 1
    end
    m
end

function primetiveroot(p::Int64)::Int64    #returns the smallest primitive root modulo a prime p
    for r = 1:p-1
        if order(r, p) == (p - 1)   #phi(p)
            return r
        end
    end
end


rootdir = Dict(zip(powermod.(primetiveroot(p), 0 : p-1, p), 0 : p-1))  #the fundamental character

ζ(k::Int64, n::Int64 = p)::Complex{Float64} = ℯ^(im*2*π*k/n)    #root of unity

χₚ = (m::Int64 -> (r::Int64 -> ζ(rootdir[r]*m, p-1)))   #a character

𝚐(χ, a = 1) = ( χ.(1 : p-1) .* ζ.(a * (1:p-1)) ) |> sum   #Gauss sum

#Plotting

using Plots
theme(:juno)

𝒢 = 𝚐.(χₚ.(1 : p-1))

Plots.scatter(√p .* ℯ .^ (im .* (0 : 2*π*100) ./ 100); aspect_ratio = 1, marker = (1, 0.6, :blue))
Plots.scatter!([0 + 0*im])
Plots.scatter!(𝒢; aspect_ratio = 1)

savefig("gauss_sums")


#Other


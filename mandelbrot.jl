using Plots

theme(:dark)

function in_bounds(c::Complex{Float64}, max_iters::Int64=100, bound::Int64=2)::Int64
    z, i = 0 + 0*im, 0
    while abs(z) < bound && i < max_iters; z = z^2 + c; i += 1; end
    i
end

pxarray = Array{Int64, 2}(undef, 400, 400)

f = (x -> (x))

function sketch(c₀::Complex{Float64}, scale::Float64)
    for i = 1:size(pxarray)[1]
        for j = 1:size(pxarray)[2]
            pxarray[i, j] = f(in_bounds(c₀ + (j + i*im)/scale))
        end
    end
end

sketch(-2.0 -1.75*im, 125.0)
Plots.heatmap(pxarray, aspect_ratio = 1)

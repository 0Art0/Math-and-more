using Plots

scale = 10
vertices = [scale .* ((z -> (real(z), imag(z)))(im * ℯ^(im * 2*π/3 * k))) for k = 0:2]

points = [[(0.0, 10.0)]]

for i  = 1:10
    new_points = Tuple{Float64, Float64}[]
    for p in points[end]
        append!(new_points, [(p .+ v) ./ 2 for v in vertices])
    end

    push!(points, setdiff!(new_points, points[end]))
end

scatter(union(points...); label = "Final Points")
scatter!(points[1]; label = "Starting point(s)")
scatter!(vertices; label = "Vertices of the triangle")

savefig("chaos_game_origin")

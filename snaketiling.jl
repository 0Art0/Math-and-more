using Pipe
using Plots

theme(:juno)

# The basic idea:
# Assign an "arrow" to each cell in the grid.
# This arrow can either point upwards (represented by "2" in the code), to the right ("1"), or in no particular direction ("0")
# If certain conditions (mentioned below) are met, one can uniquely trace out the snakes defined by these arrows and partition the grid

#Example snake for a 3 × 3 grid
# |  |  | ⊡|           ⬜
# |  | →| ↑|  ⤑     ⬜⬜
# | →| ↑|  |      ⬜⬜
#
# Legend: Up (2) - ↑, Right (1) - →, Terminal cell / Directionless arrow (0) - ⊡


#A unique map from a number to a matrix of 0s, 1s and 2s
creatematrix(n::Int64, a::Int64, b::Int64)::Array{Int64, 2} = @pipe string(n, base = 3, pad = a*b) |> split(_, "") |> parse.(Int64, _) |> reshape(_, (a, b))

#Checks if a given matrix defines a valid "snake partition"
# A matrix is invalid if:
#
# a. Snakes intersect, i.e,
# → [ ]         A configuration such as this
#    ↑                  is invalid
#
# b. A snake tries to move outside the boundaries, i.e,
#    A snake on the right edge tries to move right, or
#    A snake on the top edge tries to move up
#
function checkmatrix(m::Array{Int64, 2})::Bool
    a, b = size(m)

    for i = 1:a
        for j = 1:b
            #if snakes intersect || snake attempts to cross the upper boundary || snake attempts to cross the boundary to the right
            if ((i < a && j < b) && (m[i, j] == 1 && m[i+1, j+1] == 2)) || (i == 1 && m[i, j] == 2) || (j == b && m[i, j] == 1)
                return false
            end
        end
    end

    return true
end

#Generates all possible arrays of 0s, 1s and 2s, and retains the ones that define valid partitions
enumeratesnaketilings(a::Int64, b::Int64)::Vector{Array{Int64, 2}} = filter!(checkmatrix, creatematrix.(0:3^(a*b)-1, a, b))

#Converts a given matrix to its "coloured form" for easier visualization
function coloursnakes(mat::Array{Int64, 2})::Array{Int64,2}
    m = deepcopy(mat)
    a, b = size(m)
    v = 10

    #Trace out the snake defined by the arrows
    function coloursnake(val::Int64, pos::Tuple{Int64, Int64})
        i, j = pos

        while true
            m[i, j] = val

            if i < a && m[i+1, j] == 2
                i += 1
            elseif j > 1 && m[i, j-1] == 1
                j -= 1
            else
                break
            end
        end
    end


    for i = 1:a
        for j = 1:b
            if m[i, j] == 0
                coloursnake(v, (i, j))
                v += 10 #Assign a different colour
            end
        end
    end

    return m
end


### Plotting:

#The set of all valid m × n matrices
mats = enumeratesnaketilings(3, 3)

#Draw the matrices and save the animation as a gif
anim = @animate for (ind, mat) in enumerate(mats)
    yflip!(heatmap(coloursnakes(mat); aspect_ratio = 1))
    annotate!([(1, 1, string(ind))])
end

gif(anim, "snakeplots3x3.gif", fps = 2)

'''
    An image is represented by a 2-D array of integers, each integer representing the pixel value of the image 
    (from 0 to 65535).

    Given a coordinate (sr, sc) representing the starting pixel (row and column) of the flood fill, 
    and a pixel value newColor, "flood fill" the image.

    To perform a "flood fill", consider the starting pixel, plus any pixels connected 4-directionally 
    to the starting pixel of the same color as the starting pixel, plus any pixels connected 4-directionally 
    to those pixels (also with the same color as the starting pixel), and so on. 
    Replace the color of all of the aforementioned pixels with the newColor.

    At the end, return the modified image. 

    image = [[1,1,1],[1,1,0],[1,0,1]]
    sr = 1, sc = 1, newColor = 2
    Output: [[2,2,2],[2,2,0],[2,0,1]]
'''
class Solution:

    def solve(self, matrix, xPos, yPos, newColor):
        # define the set() values for visiting arrays
        visited = set()
        targetColor = matrix[xPos][yPos]
        self.dfs(matrix, xPos, yPos, newColor, targetColor, visited)
        return matrix

    def dfs(self, matrix, xPos, yPos, newColor, targetColor, visited):
        # add the current position to the set, so you don´t visit again
        visited.add(xPos, yPos)
        # paint the color
        matrix[xPos][yPos] = newColor
        # define the directions
        directions = [(0,1),(0,-1),(1,0), (-1,0)]
        # iterate through the directions
        for direction in directions:
            # move the x value
            newX = direction[0] + xPos
            # move the y value
            newY = direction[1] + yPos

            # validate the new position
            # make sure the current position is not in the array
            # make sure the current position is equal to the value
            if (self.validate_matrix(matrix, newX, newY) 
                and (matrix[newX][newY] == targetColor) 
                and (matrix[newX][newY] not in visited)):
                matrix[newX][newY] = targetColor
        


    def validate_matrix(matrix, xPos, yPos):
        rows = len(matrix)
        cols = len(matrix[0])

        if (xPos < 0 or yPos < 0 or xPos >= rows or yPos >= cols):
            return False
        return True




def main():
    image = [[1,1,1],[1,1,0],[1,0,1]]
    sr = 1
    sc = 1 
    newColor = 2


main()
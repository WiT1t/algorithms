
def LCS_Matrix(word1, word2):
    lcs_matrix = [[0] * (len(word2)+1)]*(len(word1)+1)
    for i in range(1, len(word1)+1):
        for j in range(1, len(word2)+1):
            if word1[i-1] == word2[j-1]:
                lcs_matrix[i][j] = lcs_matrix[i-1][j-1] + 1
            else:
                lcs_matrix[i][j] = max(lcs_matrix[i][j-1], lcs_matrix[i-1][j])
    return lcs_matrix

def construct_LCS(word1, word2, lcs_matrix, i, j):
    if lcs_matrix[i][j] == 0: return ""
    if word1[i-1] == word2[j-1]: 
        return construct_LCS(word1, word2, lcs_matrix, i-1, j-1) + word1[i-1]
    elif lcs_matrix[i-1][j] > lcs_matrix[i][j-1]:
        return construct_LCS(word1, word2, lcs_matrix, i-1, j)
    return  construct_LCS(word1, word2, lcs_matrix, i, j-1)

    

def main():
    word1 = "hello world"
    word2 = "shell mold"
    lcs = construct_LCS(word1, word2, LCS_Matrix(word1, word2), len(word1), len(word2))
    print("First word:")
    print(word1)
    print("\nSecond word:")
    print(word2)
    print("\nLCS:")
    print(lcs)


if __name__ == "__main__":
    main()
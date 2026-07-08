partitionScores :: Int -> [Int] -> [Int]
partitionScores threshold scores =
    [s | s <- scores, s <= threshold] ++ [s | s <- scores, s > threshold]

main :: IO ()
main = print (partitionScores 60 [45, 82, 60, 91, 33, 77])
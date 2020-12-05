import Utils
import Data.List

binTrav :: [Char] -> Int -> Int -> (Char, Char) -> Int
binTrav [] _ acc _ = acc
binTrav _ 0 acc _ = acc
binTrav (a:xs) n acc (one, zero)
  | a == one  = binTrav xs (n-1) (acc+2^(n-1)) (one, zero)
  | otherwise = binTrav xs (n-1) acc (one, zero)

row :: [Char] -> Int
row r = binTrav r 7 0 ('B','F')

column :: [Char] -> Int
column c = binTrav c 3 0 ('R','L')

seatID :: String -> Int
seatID s = row (take 7 s) * 8 + column (drop 7 s)

findMissing :: [Int] -> [Int] -> Int
findMissing (x:xs) (y:ys)
  | x /= y = y
  | otherwise = findMissing xs ys

main :: IO ()
main = do
    bPasses <- splitFile "data" "\n"
    let
      allSeatIDs = map seatID bPasses
     in do
      -- Problem 1
      putStrLn $ show $ (foldl1 (max) allSeatIDs)
      -- Problem 2
      putStrLn $ show $ findMissing (sort allSeatIDs) [21..996]

This folder contains a series of coding problems that I have practiced on leetcode type websites or during technical assessments that I wanted to review after the fact. They are listed below with a brief description.

## MaxSum

Given an array of integers and an integer k, return the maximum sum of any contiguous subarray of size k.

Example:<br />
Input: nums = [1, 4, 2, 10, 23, 3, 1, 0, 20], k = 4<br />
Output: 39 (because 10 + 23 + 3 + 1 = 37 is highest of any window of size 4)

## LongestSubstringNoCharRepeat

Given a string s, find the length of the longest substring without repeating characters

ex.<br />
Input: s = "abcabcbb"<br />
Output: 3

## CustomDataStructure

Design a data structure that supports insert, delete, search, and getRandom in constant time.

## QueueUsingStacks

Create a Queue (FIFO) using 2 stacks (LIFO)

## PowerSet

Given a list of integers, return all possible subsets (the power set).

## BookSort

Create a book object. This object should contain the Title, author, and genre. Create a title lookup, author lookup, and binary search for titles.

## LongestCommonPrefix

Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:

Input: strs = ["flower","flow","flight"]<br />
Output: "fl"

Example 2:

Input: strs = ["dog","racecar","car"]<br />
Output: ""<br />
Explanation: There is no common prefix among the input strings.


## Palindrome

Given an integer x, return true if x is a palindrome, and false otherwise. A palindrome is an int that reads the same forward and backward.

Constraints: <br /> 
    -2^31 <= x <= 2^31 - 1


## TwoSum

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.

Constraints: <br /> 
    2 <= nums.length <= 10^4 <br /> 
    -10^9 <= nums[i] <= 10^9 <br /> 
    -10^9 <= target <= 10^9 <br /> 
    Only one valid answer exists.

## LinkedList

Create a simple linked list that contains a value and is aware of the next node in the list.

## BracketCombinations

Have the function BracketCombinations(num) read num which will be an integer greater than or equal to zero, and return the number of valid combinations that can be formed with num pairs of parentheses. For example, if the input is 3, then the possible combinations of 3 pairs of parenthesis, namely: ()()(), are ()()(), ()(()), (())(), ((())), and (()()). There are 5 total combinations when the input is 3, so your program should return 5.

## ReactCounter

Make the counter increase every time the button is pressed in JS

## RomanNumerals

Have the function BasicRomanNumerals(str) read str which will be a string of Roman numerals. The numerals being used are: I for 1, V for 5, X for 10, L for 50, C for 100, D for 500 and M for 1000. In Roman numerals, to create a number like 11 you simply add a 1 after the 10, so you get XI. But to create a number like 19, you use the subtraction notation which is to add an I before an X or V (or add an X before an L or C). So 19 in Roman numerals is XIX. The goal of your program is to return the decimal equivalent of the Roman numeral given. For example: if str is "XXIV" your program should return 24

## ApproachingFibonacci

Have the function ApproachingFibonacci(arr) take the arr parameter being passed which will be an array of integers and determine the smallest positive integer including zero that can be added to the array to make the sum of all of the numbers in the array add up to the next closest fibonacci number

## AWSRetrieveS3BucketFilename

Access a public S3 Bucket and print all filenames that start with "\_\_cb\_\_"

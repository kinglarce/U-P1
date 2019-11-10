This problem said to create a "tree" and I'm going to get the code from that tree which is determined by the frequency of the characters. As suggested in the problem, my implementation data structure uses Binary Tree where the encoded character being stored on the leaves and Recursion for traversing the tree and getting the codes. It consists of grabbing the characters from the input and put them in the list, sort by usage(frequency), built a tree by dividing them, and finally traversing that tree to trim it(remove frequency) and determine the codes for each character. 

Both encoding and decoding time complexity will take O(n log(n)) where the n is the number of characters and log(n) is the iteration requires. The space would be O(n) as it's determined by the input/data.


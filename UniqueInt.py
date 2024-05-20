class UniqueInt:
    def processFile(self, inputFilePath, outputFilePath):
        # Create a boolean array to track unique integers
        seen = [False] * 2048

        # Read input file and identify unique integers
        with open(inputFilePath, 'r') as inputFile:
            for line in inputFile:
                line = line.strip()
                if line and line.replace('-', '', 1).isdigit():
                    integer = int(line)
                    if integer >= -1023 and integer <= 1023 and not seen[integer + 1023]:
                        seen[integer + 1023] = True

        # Write unique integers to output file in sorted order
        with open(outputFilePath, 'w') as outputFile:
            for i in range(2048):
                if seen[i]:
                    outputFile.write(str(i - 1023) + '\n')

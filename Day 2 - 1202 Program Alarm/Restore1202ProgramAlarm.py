from InputData import puzzelData as inputData

SEGMENT_OP_CODE = 0
SEGMENT_NUM1 = 1
SEGMENT_NUM2 = 2
SEGMENT_RESULT_POSITION = 3
SEGMENT_SIZE = 4

def GetOpCode(segment):
    return segment[SEGMENT_OP_CODE]

def GetNum1(segment):
    return segment[SEGMENT_NUM1]

def GetNum2(segment):
    return segment[SEGMENT_NUM2]

def GetResultPostion(segment):
    return segment[SEGMENT_RESULT_POSITION]

def OpCode1(num1, num2):
    return num1 + num2

def OpCode2(num1, num2):
    return num1 * num2

def OpCode99():
    return -1

Opperation = [0, OpCode1, OpCode2]

def CalculateOpCodeSegments(length):
    return length // SEGMENT_SIZE

def CalculateUpperBoundary(segmentIndex):
    return segmentIndex * SEGMENT_SIZE

def CalculateLowerBoundary(upperBoundary):
    return upperBoundary - SEGMENT_SIZE

def GetSegment(upperBoundary, lowerBoundary):
    return inputData[lowerBoundary:upperBoundary]

def ProcessOpcode(opCode, segment, inputData):
    return Opperation[opCode](inputData[segment[SEGMENT_NUM1]], inputData[segment[SEGMENT_NUM2]])

def RestoreProgramAlarm(inputData):
    numberOfSegments = CalculateOpCodeSegments(len(inputData))

    for segmentIndex in range(1, numberOfSegments):
        segment = GetSegment( \
                    CalculateUpperBoundary(segmentIndex), \
                    CalculateLowerBoundary(CalculateUpperBoundary(segmentIndex)) \
                    )
        if GetOpCode(segment) == 99:
            break
        else:
            inputData[segment[SEGMENT_RESULT_POSITION]] = ProcessOpcode(GetOpCode(segment), segment, inputData)
    return inputData[0]

if __name__ == "__main__":
    for x in range(0, 99):
        for y in range(0, 99):
            copyInputData = inputData.copy()
            copyInputData[1] = x
            copyInputData[2] = y
            if RestoreProgramAlarm(copyInputData) == 19690720:
                noun = x
                verb = y
                break
    print("Noun: {}, Verb: {}, Result: {}".format(noun, verb,((100*noun)+verb)))

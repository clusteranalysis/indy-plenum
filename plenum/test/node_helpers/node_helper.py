from plenum.test.helper import TestNode


def getProtocolInstanceNums(node: TestNode):
    return [node.masterInst, *node.nonMasterInsts]
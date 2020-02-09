NeoIOCommands = {1:'WRITE', 2:'READ', 9:'DSM'}

NeoIOVscCommands = {132:'LbaReservation', 136:'DeleteReservation', 138:'GetNandInfo', 161:'UpdateFw', 166:'ReadFw', 142:'GetControllerInfo', 145:'SetControllerInfo', 178:'ReadLut', 146:'ReadSram', 149:'WriteSram', 154:'ReadDDR', 157:'WriteDDR', 208:'ReadPage', 212:'WritePage', 216:'WriteMultiPlane', 220:'EraseBlock', 224:'EraseMultiPlaneBlock', 228:'EraseResume', 232:'SetRefData', 236:'GetRefData', 240:'ReadLong'}

NeoAdminCommands = {0:'DeleteIoSubmissionQueue', 1:'CreateIoSubmissionQueue', 2:'GetLogPage', 3:'DeleteIoCompletionQueue', 4:'CreateIoCompletionQueue', 6:'MvmeIdentify', 7:'NvmeAbort', 8:'SetFeatures', 9:'GetFeatures', 10:'EventRequest', 11:'NvmeFormat'}

NeoAdminVscCommands = {192:'GeneralCommand', 196:'VscSetting', 200:'VscUtil', 240:'MarvellCommand'}

eventIDDictionary = {1:'EndPhase1', 2:'EndPhase2', 3:'EndPhase3', 4:'EndPhase4', 5:'EndPhase5', 16:'CreateLogicalPartition', 17:'DeleteLogicalPartition', 18:'ExpandLogicalPartition', 19:'ActivatePartition', 20:'DeactivatePartition', 21:'EraseSuperBlock'} #, 22:'BlockWriteStart', 23:'BlockWriteEnd', 24:'StartGC', 27:'StartMediaScan', 55:'ExpirePhaseTimeout'}

eventIDDictionary2 = {10:'cEventTypeSTCopyStart', 11:' cEventTypeSTCopyStartParam1', 12:' cEventTypeSTCopyStartParam2', 13:'cEventTypeSTCopyEnd', 14:'cEventTypeSTCopyEndParam1', 15:'cEventTypeSTCopyEndParam2', \
   20:'cEventTypeGCstart', 21:' cEventTypeGCEnd', 30:' cEventTypeRDreadScanStart', 32:'cEventTypeRDreadScanEnd', 34:'cEventTypeRDstartCopy', 35:'cEventTypeRDstartParam1', 36:'cEventTypeRDendCopy', 37:'cEventTypeRDendParam1', \
    40:'cEventReadDisturbReach1k', 50:'cEventReadDisturbReach16k', 60:' cEventTypeStartMediaScan ', 61:'cEventTypeStartMediaScanParam1', 62:'cEventTypeEndMediaScan', 63:'cEventTypeEndMediaScanParam1', 64:'cEventTypeStartCopy', 65:'cEventTypeStartCopyParam1', 66:'cEventTypeEndCopy', 67:'cEventTypeEndCopyParam1', \
     70:'cEventRebuildMetadata', 80:'cEventTypePSAllocatedStart', 81:'cEventTypePSAllocatedStartParam1', 90:'cEventTypePSDeallocatedStart', 91:'cEventTypePSDeallocatedStartParam1', 100:'cEventTypeDefectBlockDetectParam1',101:'cEventTypeDefectBlockDetectParam2', 102:'cEventTypeDefectBlockDetectParam3', \
       110:'cEventTypeNVMeReadCommandId', 112:'cEventTypeECU_Success', 113:'cEventTypeECU_ErrorRetry',114:'cEventTypeECU_ReadRetry', 120:'cEventTypeNVMeWriteCommandId', 122:'cEventTypeWrite_Success',130:'cEventWearLeveling', 140:'cEventTypeL2Ptable', 141:'cEventTypePhysicalBlockManagement', \
        150:'cEventTypeEraseStart', 151:'cEventTypeEraseEnd', 152:'cEventTypeEraseSuspend', 153:'cEventTypeEraseResume', 150:'cEventTypeEraseStart2nd', 151:'cEventTypeEraseEnd2nd', 160:'cEventProgramSuspend', 170:'cEventTypeLogicalPartitionCreateStart', 171:'cEventTypeLogicalPartitionCreateEnd', 172:' cEventTypeLogicalPartitionDeleteStart', \
                                    173:'cEventTypeLogicalPartitionDeleteEnd', 174:'cEventTypeLogicalPartitionExpandStart', 175:'cEventTypeLogicalPartitionExpandEnd', 176:'cEventTypeLogicalPartitionEraseStart', 177:'cEventTypeLogicalPartitionEraseEnd',  \
                                                  180:'cEventTypeLogicalPartitionActivateStart', 181:' cEventTypeLogicalPartitionActivateEnd', 182:'cEventTypeLogicalPartitionDeactivateStart', 183:'cEventTypeLogicalPartitionDeactivateEnd', 190:'cEventTypeReservationCreateStart', 191:'cEventTypeReservationCreateEnd', 192:'cEventTypeReservationDeleteStart', 193:'cEventTypeReservationDeleteEnd', \
                                                                200:'cEventLogicalPartitionBackgroundBob', 210:'cEventTypeSetNandEvaluationMode', 280:'cEventTypeReadPhysicalPageSubmit', 281:'cEventTypeReadPhysicalPageComplete', 282:'cEventTypeSetCorrectbuffer', 290:'cEventTypeProgramMultiPlanePhysicalPageSubmit', 291:'cEventTypeProgramMultiPlanePhysicalPageComplete', 292:'cEventTypeProgramPhysicalPageSubmit', 292:'cEventTypeProgramPhysicalPageComplete', \
                                                                300:'cEventTypeEraseMultiPlanePhysicalBlockSubmit', 301:'cEventTypeEraseMultiPlanePhysicalBlockComplete', 302:'cEventTypeErasePhysicalBlockSubmit', 303:'cEventTypeErasePhysicalBlockComplete', 304:'cEventTypeEraseResumeSubmit', 305:'cEventTypeEraseResumeComplete', 310:'cEventTypeSetReferenceDataSubmit', 311:'cEventTypeSetReferenceDataComplete', \
                   312:'cEventTypeGetReferenceDataSubmit', 313:'cEventTypeGetReferenceDataComplete', 314:'cEventTypeReadLongSubmit', 315:'cEventTypeReadLongComplete', 330:'cEventTypeReceivedCloseNandAccess', 331:'cEventTypeFlushMetadata', 332:' cEventTypeCloseNandAccessDone', 340:'cEventTypeWriteErrorHandlingStart', 341:'cEventTypeSuperBlockCopyStart', 342:'cEventTypeCopyStartParam1', \
                    343:'cEventTypeSuperBlockCopyEnd', 344:'cEventTypeWriteErrorHandlingEnd', 350:'cEventTypeRebuildNumberOfSuperblocksTotal', 351:'cEventTypeRebuildNumberOfSuperblocksDone', 360:'cEventFreeSuperblockCountUpdated', 370:'cEventWriteEventWithLabel', 380:'cEventTypeStaticManStartCopy', 381:'cEventTypeStaticManStartCopyParam1', 382:'cEventTypeStaticManStartCopyParam2', 383:'cEventTypeStaticManEndCopy', \
                    384:'cEventTypeStaticManEndCopyParam1', 385:'cEventTypeStaticManEndCopyParam2', 390:'cEventTypeRaidRecoveryFailureAddressLowDWord', 391:'cEventTypeRaidRecoveryFailureAddressHighDWord', 392:'cEventTypeRaidRecoveryResult', 400:'cEventTypeRefreshReadOperationStart', 401:'cEventTypeRefreshReadOperationEnd', 410:'cEventTypeCopyEngineUnrecoverableReadError', 411:'cEventTypeCopyEngineUnrecoverableReadErrorParam1', 412:'cEventTypeCopyEngineUnrecoverableReadErrorParam2', \
                      413:'cEventTypeCopyEngineUnrecoverableReadErrorParam3', 600:'cEventDebugLogBegin',610:'cEventDebugLogMiddle', 620:'cEventDebugLogEnd', 630:' cEventDebugLogOne'}

def ProcessTheNotificationAndEventBuffers(j, k, bufferData, fileName):
# Here we're going to preprocess the data to find out where the notification and event buffers are.
# This is done by looking for 16 byte MemWrs from the drive.
    bufferSize = 65536

    lineLength = 1

    minValueBuffer0 = 1000000

    minValueBuffer1 = 1000000

    buffer0Start = 0

    buffer1Start = -1

    lastIndex = -1

    lastAddress = 0

    a = open('CommandFifo.txt', 'w')

    b = open('Status.txt', 'w')

    c = open('Events.txt', 'w')

    print('Scanning the file for Events and Notifications. This takes about 1 min. ')

 

    while (lineLength != 0):

#    for pp in range(0,4000000):

        myVar1 = j.readline()

        lineLength = len(myVar1)

        if (lineLength == 0):

                        break

 

        firstHit = myVar1.find('MWr(64)')

        secondHit = myVar1.find('Upstream')

        thirdHit = myVar1.find('MWr')

        fourthHit = myVar1.find('MRd')

        if (((firstHit > -1) | (thirdHit > -1)) & (secondHit > -1) | (fourthHit > -1)):

            myNewLineSplit = myVar1.split(',')

            tpLength = int(myNewLineSplit[24], 10)

            seqNumber = myNewLineSplit[1]

           

            address = myNewLineSplit[28]

            address = address.replace(':', '')

            addressInHexAll = int(address,16)

            addressInHex = (int(address, 16)) & 0xffffffff

            addressInHexHigh = (int(address, 16)) & 0xffffffff00000000

            addressInHex = int(addressInHex)

            data = myNewLineSplit[len(myNewLineSplit)-7].split()

            if(tpLength == 2):

                eventID = int(data[1], 16) & 0x3f

                timeStamp = (int(data[1], 16) & 0xFFFFFFC0)/64

                key = eventID

                if (key in eventIDDictionary):

                    eventString = eventIDDictionary[key]

 

                    temp = addressInHex % bufferSize

                    bufferIndex = temp/8

#                    k.write('{:10s}'.format(seqNumber) +  '{:30s}'.format(address) + '{:20s}'.format(data[0]) + '{:20s}'.format(str((timeStamp))) + '{:30s}'.format(eventString) + '{:10s}'.format(str(hex(int(bufferIndex)))) + '\n')   

                    if (lastIndex != -1):

                        if(bufferIndex == lastIndex + 1):

                            if (buffer0Start == 0):

                                buffer0Start = addressInHex - bufferIndex*8 + addressInHexHigh                                                                      

                    if (lastAddress > 0):

                        if (abs(addressInHex - lastAddress) > bufferSize):

                            if (buffer1Start == -1):

                                buffer1Start = addressInHex - bufferIndex*8    + addressInHexHigh                                                                                       

                    lastIndex = bufferIndex

                    lastAddress = addressInHex

            # 64 byte MWr.  Could be notification or status.

            if((tpLength == 4) & (firstHit > 1)):

                data0 = int(data[0], 16)

                data1 = int(data[1], 16)                             

                if ((data0 != 0) | (data1 != 0)):

                    c.write(str(hex(addressInHexAll)) + '\n')

                  

            #  16 word memory reads.  Command FIFO

            if((tpLength == 16) & (fourthHit > 1)):

                a.write(str(hex(addressInHexAll)) + '\n')

               

                                                #  MWr, could be status write or notification write.  D0 and D1 on status write are 0.

            if((tpLength == 4) & (thirdHit > 1)):

                data0 = int(data[0], 16)

                data1 = int(data[1], 16)                             

                if ((data0 == 0) & (data1 == 0)):

                    b.write(str(hex(addressInHexAll)) + '\n')

                    if (abs(addressInHexAll - 0x173240000) < 1000000):

                        print('Found it')

                        print(seqNumber)

 

                   

    a.close()

    b.close()

    c.close()

    return (buffer0Start, buffer1Start)                     

def ProcessCommandAndStatus(j, k, bufferData, fileName, commandQueues, commandQueueCnt, statusQueues, statusQueueCnt):

# Here we're going to preprocess the data to find out where the notification and event buffers are.

# This is done by looking for 16 byte MemWrs from the drive.

 

 

    j.seek(0)

    bufferSize = 65536

    lineLength = 1

    minValueBuffer0 = 1000000

    minValueBuffer1 = 1000000

    buffer0Start = 0

    buffer1Start = -1

    lastIndex = -1

    lastAddress = 0

    a = open('CommandFifo.txt', 'w')

    b = open('Status.txt', 'w')

    c = open('Events.txt', 'w')

    print('Scanning the file for Events and Notifications. This takes about 1 min. ')

 

    while (lineLength != 0):

#    for pp in range(0,4000000):

        myVar1 = j.readline()

        lineLength = len(myVar1)

        if (lineLength == 0):

                        break

 

        firstHit = myVar1.find('MWr(64)')

        secondHit = myVar1.find('Upstream')

        thirdHit = myVar1.find('MWr')

        fourthHit = myVar1.find('MRd(32)')

        if (((firstHit > -1) | (thirdHit > -1)) & (secondHit > -1) | (fourthHit > -1)):

            myNewLineSplit = myVar1.split(',')

            tpLength = int(myNewLineSplit[24], 10)

            seqNumber = myNewLineSplit[1]

           

            address = myNewLineSplit[28]

            address = address.replace(':', '')

            addressInHexAll = int(address,16)

            addressInHex = (int(address, 16)) & 0xffffffff

            addressInHexHigh = (int(address, 16)) & 0xffffffff00000000

            addressInHex = int(addressInHex)

            data = myNewLineSplit[len(myNewLineSplit)-7].split()

            # 64 byte MWr.  Probably events and notifications.

            #  16 word memory reads.  Command FIFO

            if((tpLength == 16) & (fourthHit > 1)):

                (queue, index) = FindTheSlot(addressInHexAll, commandQueues, commandQueueCnt, 64, 256*64)

                a.write(seqNumber + '   ' + str(queue) + '   ' + str(index)  + '\n')

 

 

 

                                                # MWr, either status or notifications.

            if((tpLength == 4) & (thirdHit > 1)):

                data0 = int(data[0], 16)

                data1 = int(data[1], 16)

                if ((data0 == 0) & (data1 == 0)):

                    (queue, index) = FindTheSlot(addressInHexAll, statusQueues, statusQueueCnt, 16, 512*16)

                    b.write(seqNumber + '   ' + str(queue) + '   ' + str(int(index))  + '    ' + data[3] + '\n')

 

                   

    a.close()

    b.close()

    c.close()

    return (buffer0Start, buffer1Start)                     

def FindTheSlot(address, queueArray, queueCnt, entrySize, queueSize):

 

    mask = 0xFFFFFFFFF - (queueSize - 1)

    slot = -1

    queue = -1

    addressTarget =address & mask

    for i in range(0,queueCnt):

        if (addressTarget == int(queueArray[i], 16)):

            queue = i

            slot = (address - int(queueArray[queue], 16)   )/entrySize

            return (queue, slot)

    return (queue, slot)   

def ProcessTheCommandFIFO():

 

   a = open('CommandFIFO.txt', 'r')

   buffer = a.read()

   print(len(buffer))

   print(buffer[0:40])

   a.close

   return (0, 0)

def ExtractAQueue(fileName, queueDepth, entrySize, addressRanges, queueDepths):
    a = open(fileName, 'r')

    buffer = a.read()

    a.close()

 

    buffer = buffer.replace('  ', '')

    buffer = buffer.split('\n')

 

    length = len(buffer)

    maxValue = max(buffer)

    print(str(maxValue))

    print(buffer.index(maxValue))

 

    minValue = min(buffer[0:length-1])

    print(buffer.index(minValue))

    print(str(minValue))

 

    print(addressRanges[0])

    queueDepth1 = queueDepth * entrySize

   

    for i in range(0, length-1):

        temp = (hex( int(buffer[i], 16) & (0xFFFFFFFFFFFFFFFF - (queueDepth1 -1))))

        addressInHex = int(buffer[i], 16)

        try:

            currentOffset = addressRanges.index(0)

        except ValueError:

            currentOffset = -1

        try:

            isTheValueAlreadyThere = addressRanges.index(temp)

        except ValueError:

             isTheValueAlreadyThere = -1

 

 

 

        if(isTheValueAlreadyThere == -1):

            addressRanges[currentOffset] = temp

 

 

        CountTheSlots(addressInHex, entrySize, addressRanges, queueDepths, queueDepth1)

   

    for i in range(0,10):

        if (addressRanges[i] == 0):

            queueCount = i

            break

def SanityCheckTheQueues(commandQueues, commandQueueDepths, commandQueueCnt, statusQueues, statusQueueDepths, statusQueueCnt):
    if (statusQueueCnt == commandQueueCnt):
                    return
    if (statusQueueCnt > commandQueueCnt):
        maxLen = statusQueueCnt
        error = 'Status Queue'
    else:
        maxLen = commandQueueCnt
        error = 'Command Queue'
    for i in range (0, maxLen):
        if ((abs(commandQueueDepths[i] - statusQueueDepths[i]) > 4)):
            print('Here is the error')
            print(commandQueues[i])
            print(statusQueues[i])
            break

    if (error == 'Status Queue'):
        for k in range(i, maxLen):
            statusQueues[k] = statusQueues[k + 1]
            statusQueueDepths[k] = statusQueueDepths[k + 1]
    else:
        for k in range(i, maxLen):
            commandQueues[k] = statusQueues[k + 1]
            commandQueueDepths[k] = statusQueueDepths[k + 1]

def FindTheQueueAndSlot(queuesInUse, queueCount, address, queueDepth, entrySize):

 

    #Find out which of the queues contains the current address.

    addressInHex = address

    for i in range(0, queueCount):

        if (type(queuesInUse[i]) == str):

            diff = abs(int(addressInHex, 16) - int(queuesInUse[i], 16))

            if (diff < queueDepth):

                slot = diff/entrySize

                return i, slot   

def CountTheSlots(addressInHex, slotEntrySize, queueAddresses, queueMaxValues, queueDepth):
    #Find out which of the queues contains the current address.
    for i in range(0, 10):
        if (type(queueAddresses[i]) == str):
            diff = addressInHex - int(queueAddresses[i], 16)
            if (diff < queueDepth):
                slot = diff/slotEntrySize
                if (slot > queueMaxValues[i]):
                    queueMaxValues[i] = slot

def FindTheCommandHere(commandData):
    neoCommand = ''
    additionalString = ''
    key1 = (int(commandData[0], 16) & 0xFF)
    NSID = (int(commandData[1], 16))
    if ((key1 in NeoIOCommands) & (NSID < 4)):
        neoCommand=NeoIOCommands[key1]
        additionalString = ProcessIOCommand(commandData)
        additionalString = additionalString + '   ' + 'NSID  ' + str(NSID)
    if (key1 in NeoIOVscCommands):
        neoCommand=NeoIOVscCommands[key1]
        additionalString = ProcessNeoIOVscCommand(commandData, neoCommand)

 

    if ((key1 in NeoAdminCommands) & (NSID == 0)):

        neoCommand=NeoAdminCommands[key1]

        additionalString = ProcessNeoAdminCommand(commandData)

    if (key1 in NeoAdminVscCommands):

        neoCommand=NeoAdminVscCommands[key1]

        additionalString = ProcessNeoAdminVscCommand(commandData, neoCommand)

    return neoCommand + additionalString

def ProcessIOCommand(commandData):
    returnString = ''
    lba = (int(commandData[11], 16)<<32) + int(commandData[10], 16)
    count = (int(commandData[12], 16) & 0xFFFF) + 1
    returnString =  '   LBA   ' +    str(hex(lba)) + '    count ' +  str(hex(count))
    return returnString

def ProcessNeoIOVscCommand(commandData, vscIoCommand):
    VscIOCommandDictionary = {}
    categoryDictionary = {0:'GeneralInfo', 1:'FwStatusInfo', 2:'VendorUniqueSmart', 3:'ModuleErrorLog'}
    nandCategoryDictionary = {0:'AllNandInformation', 1:'ManufacturerId', 2:'IdentifierCode', 3:'ParameterPage', 4:'SpecficConfiguration', 5:'DriverStrengthSetting', 6:'ExternalVppSetting', 7:'TimingMode', 8:'VolumeConfiguration', 9:'ReadyBusyPullDownStrength', 10:'ReadRetrySetting', 11:'ArrayOperationMode', 12:'AutoReadCalibration', 13:'FlagCheckFunctionality', 14:'SleepVccqMode', 15:'TemperatureSensor', 16:'SnapReadMode', 17:'SleepLiteFeature'}
    returnString = ''
    additionalString = ''
    if (vscIoCommand == 'GetControllerInfo'):
        type = int(commandData[14], 16) & 0xfffff
        category = (int(commandData[14], 16)>>24)
        if (category in categoryDictionary):
            additionalString = '    ' + categoryDictionary[category]

    if (vscIoCommand == 'GetNandInfo'):
        type = int(commandData[14], 16)
        if (type in nandCategoryDictionary):
            additionalString = '    ' + nandCategoryDictionary[type]
    return returnString     + additionalString

def ProcessNeoAdminCommand(commandData):
    returnString = ''
    return returnString

def ProcessNeoAdminVscCommand(commandData, neoCommand):
    phase1ParamDictionary = {1:'disableNsid1rInPhase2', 2:'disableNsid1wInPhase2', 4:'disableNsid2wInPhase2', 8:'disableNsid3rInPhase2', 16:'disableNsid3wInPhase2', 32:'disableNsid3rtInPhase2', 64:'disablePhase4', 128:'disableHighPriorityPhase5', 256:'disableBgJobsPhase3_5'}
    VscAdminCommandGeneralDictionary = {1:'EndPhase1', 4:'EndPhase4', 16:'CreateLogicalPartition', 17:'DeleteLogicalPartition', 18:'ExpandLogicalPartition', 19:'ActivatePartition', 20:'DeactivatePartition', 21:'EraseSuperBlock', 22:'BlockWriteStart', 23:'BlockWriteEnd', 24:'StartGarbageCollection', 27:'StartMediaScan', 30:'WriteEventNotificationWithLabel'}
    VscAdminSettingCommandDictionary = {50:'GetBlockSize', 51:'SetOverrunInterval', 52:'SetAutomaticSuspend', 53:'SetGarbageCollectionThreshold', 54:'SetReadDisturbThreshold', 55:'SetPhaseTimeout', 56:'SetNandEvaluationMode', 57:'SetCorrectableBitBuffer', 58:'SetMediaScanThreshold', 59:'GetReservation', 60:'SetStaticManMode', 64:'SetNotificationBuffer', 65:'FilterNotificationBuffer', 66:'SetNotificationBufferInterrupt', 67:'SetEventBuffer', 68:'FilterEventBuffer', 69:'SetEventBufferInterrupt', 70:'SetNotificationFrequency', 71:'SetEventFrequency'}
    VscAdminUtilCommandDirectory = {80:'OpenCloseNANDaccess', 96:'NandFormat', 97:'Diagnostic', 98:'SetDebugLogMode', 99:'SetTestPlanMode', 100:'StartRaidCheck', 101:'SetFwDataDebugMode'}
    key2 = -1
    returnString = ''
    addedString = ''
    paramString = ''
    key = int(commandData[12], 16) & 0xff
    if (neoCommand == 'GeneralCommand') & (key in VscAdminCommandGeneralDictionary):
        addedString =  VscAdminCommandGeneralDictionary[key]
        returnString = '    ' + addedString
    if (neoCommand == 'VscSetting') & (key in VscAdminSettingCommandDictionary):
        returnString = '    ' + VscAdminSettingCommandDictionary[key]
    if (neoCommand == 'VscUtil') & (key in VscAdminUtilCommandDirectory):
        returnString = '    ' + VscAdminUtilCommandDirectory[key]

    if (addedString == 'EndPhase1'):
        key2 = int(commandData[13], 16)
        if (key2 in phase1ParamDictionary):
            paramString = phase1ParamDictionary[64]
            returnString = returnString + '    ' + paramString
    return returnString

 def ProcessTheLine(myNewLine, arrayOfCommandData, k, readArray, m, interruptCount, buffer1, buffer2, commandQueues, commandQueueCnt, queueInUse, slot):

 

    sectorSize = 4096   

    arrayOfCommandData[1] = ''

  

    commandType = 'IO'

    firstHit = myNewLine.find('MRd')

    secondHit = myNewLine.find('MWr(32)')

    thirdHit = myNewLine.find('CplD')

    fourthHit = myNewLine.find('MWr(64)')

    fifthHit = myNewLine.find('Upstream')

    sixthHit = myNewLine.find('Downstream')

    tpLength = 0

    secondHit = -1

 

 

 

#    print(myNewLine)

    if ((firstHit > -1) | (secondHit > -1) | (thirdHit > -1) | (fourthHit > -1)):

 

        myNewLineSplit = myNewLine.split(',')   

        time = myNewLineSplit[len(myNewLineSplit)-5]

        myNewLineSplit[28] = myNewLineSplit[28].replace(':','')

        tpLength = int(myNewLineSplit[24], 10)

        seqNumber = myNewLineSplit[1]

 

 

 

 

        if (firstHit > -1):

 

 

            addressForRead = int(myNewLineSplit[28], 16)

 

            tagForRead = int(myNewLineSplit[26], 10)

            readArray[0]= tagForRead

            readArray[1] = addressForRead

 

        if ((tpLength == 1) & (secondHit > -1)):           

            addressData = myNewLineSplit[len(myNewLineSplit)-1].split()

            address =int(myNewLineSplit[28], 16)

            highAddress = address & 0xFFFF0000

            highTarget = 314156

 

            if (highAddress == highTarget):

 

                print(hex(address))

                interruptCount = interruptCount + 1

                m.write('Type 3 ' + str(address) + ' ' + str(interruptCount) + '\n')

                print("Here")

                print(interruptCount)

           

        

 

                                # Memory read to fetch commands, mostly.

        if ((tpLength == 16) & (firstHit > -1) & (fifthHit > -1)):

            address =(myNewLineSplit[28])

            (queueInUse, slot) = FindTheQueueAndSlot(commandQueues, commandQueueCnt, address, (256 * 64), 64)

            return queueInUse, slot

                                # Completion that returns command info.

        if ((tpLength == 16) & (thirdHit > -1)):

            commandData = myNewLineSplit[len(myNewLineSplit)-7].split()

#           print(myNewLineSplit)

            currentTag = int(myNewLineSplit[26], 10)

 

            commandString = ''

            

            commandString = FindTheCommandHere(commandData)

 

           

            commandID = 0

                       

            if ((commandString != '')):

                lba = commandData[10]

                address =(myNewLineSplit[28])

 

                count = ((int(commandData[12], 16) + 1) & 0x0FFFFFFF)

                m.write('{:10s}'.format(seqNumber) + '{:60s}'.format(commandString) + '{:20s}'.format(time) +  '{:10s}'.format(str(int(slot))) +  '{:10s}'.format(str(queueInUse))  + '{:10s}'.format('Status') + '\n')

 

 

        if ((fourthHit > -1) & (fifthHit > -1)):

 

            address = myNewLineSplit[28]

            address = address.replace(':', '')

            address = int(address, 16)

            eventString = ''

            if ((abs(address - buffer1) < 65536) | (abs(address - buffer2) < 65536)):

            #    print('Event or Notification')

                data = myNewLineSplit[len(myNewLineSplit)-7].split()

                timeStamp = (int(data[1], 16)>>6)

                data0 = data[0]

                data1 = data[1]

                OutputEventOrNotification(m, data0, data1, timeStamp, seqNumber, buffer1, buffer2, address, time)

                if (tpLength == 4):

                  

                    data0 = data[2]

                    data1 = data[3]

                    OutputEventOrNotification(m, data0, data1, timeStamp, seqNumber, buffer1, buffer2, address, time)                   

 

            

        return  queueInUse, slot

       

    return queueInUse, slot

def OutputEventOrNotification(m, data0, data1, timeStamp, seqNumber, buffer1, buffer2, address, time):

 

    eventString = ''

    eventID = int(data1, 16) & 0x3f

    if ((abs(address - buffer1) < 65536)):

        eventLowNibble = int(data0, 16)>>28

        key = eventLowNibble + eventID*10

        if (key in eventIDDictionary2):

            eventString = eventIDDictionary2[key]

        if ((eventID == 11) & (eventLowNibble == 12)):

            eventString = 'cEventTypeECU_ReadRetryMcrc'

    else:

        key = eventID

        if (key in eventIDDictionary):

            eventString = eventIDDictionary[key]

                    

 

    index1 = (address - buffer1)

    index2 = (address - buffer2)

    if ((index1 < 65536) & (index1 > 0)):

        index1 = (address - buffer1)/8

        m.write('{:10s}'.format(seqNumber) + '{:100s}'.format('Event    ' + eventString + '    Index  ' + str((int(index1))) + '  Timestamp   ' + str(hex(int(timeStamp)))) + '{:s}'.format(time) + '\n')

    if ((index2 < 65536) & (index2 > 0)):

        index2 = (address - buffer2)/8

        m.write('{:10s}'.format(seqNumber) + '{:100s}'.format('Notification    ' + eventString + '    Index  ' + str((int(index2))) + '  Timestamp   ' + str(hex(int(timeStamp)))) + '{:s}'.format(time) + '\n')

def PairStatusWithCommands(fileOne, fileTwo, m):

#             fileOne is a list of commands indexed by sequence number. It contains queue and slot info for each command

#   fileTwo contains a list of status responses indexed by sequence number containing queue and slot info.

#   This subroutine finds the status for each command by matching sequence, queue and slot.

 

 

 

    a = open(fileOne, 'r')

    b = open(fileTwo, 'r')

 

 

    statusBuffer = b.read()

    statusBufferLength = statusBuffer.count('\n')

    statusBuffer = statusBuffer.split('\n')

 

    print('Total number of Status to process. ', statusBufferLength)

 

    commandLineCount = 0

    searchStart = 0

    statusBufferCount = 0

 

    length = 10

    while (length != 0):

    #for i in range(0, 10000):

 

        myVar1 = a.readline()

        commandLineCount = commandLineCount + 1

        if (len(myVar1) == 0):

            break

 

        hit1 = myVar1.find('Status')

        if (hit1 < 1):

            m.write(myVar1 + '\n')

            continue

 

        myVar1Split = myVar1.split()

        myVar1Split2 = myVar1.split(' ')

 

        for i in [i for i,x in enumerate(myVar1Split) if x == 'Status']:

            status = i

        queue = myVar1Split[status - 1]

        slot  = myVar1Split[status - 2]

        seqNumber = myVar1Split[0]

 

    

    #  Here we know the value of sequence number, queue and slot we need to match with the status.

   

        for kk in range(searchStart, statusBufferLength):

 

            myVar2 = statusBuffer[kk]

 

            myVar2Split         = myVar2.split()

            statusSeqNumber     = myVar2Split[0]

            statusQueueNumber   = myVar2Split[1]

            statusSlotNumber    = myVar2Split[2]

            actualStatus        = myVar2Split[3]

 

            if (statusSeqNumber < seqNumber):

                       

                continue

 

            if ((slot == statusSlotNumber) & (queue == statusQueueNumber)):

 

                myVar1Split[status] = actualStatus

                for jj in [jj for jj,x in enumerate(myVar1Split2) if x == 'Status']:

                   statusIsHere = jj

                   myVar1Split2[statusIsHere] = '    ' + str(hex(int((int(actualStatus, 16) & 0xFFFF0000)/2/65536)))

                m.write(' '.join(myVar1Split2) + '\n')

                statusBufferCount = statusBufferCount + 1

                if ((statusBufferCount % 1000) == 0):

                    print('Total Status Processed  ', statusBufferCount, ' Total lines  ', statusBufferLength)

                if (statusBufferCount > 100):

                    searchStart = statusBufferCount - 100

                break

 

    a.close()

    b.close()

 

    return  

################################ main loop ########################################
import binascii
import math
inputFile1 = "Ross2.csv"
outputFile = "Notification.out"
outputFile1 = "Ross2.out"
outputFile2 = "Temp.out"

j = open(inputFile1,"r")
k = open(outputFile, "w")
m = open(outputFile1, 'w')
n = open(outputFile2, 'w')
m.write('This program analyzes data from a Lecroy and tries to construct a trail of OS activity. \n')
m.write('We scan the entire trace to extract address for command and status queues, and event and notification buffers. \n')
m.write('Temporary files are created for command queue addresses(CommandFIFO.txt), status queues(Status.txt) and \n')
m.write('events and notifications(Events.txt).  \n')

arrayOfCommandData = ['' for x in range(0,10)]
readArray = [0 for x in range(0,2)]
bufferData = [0 for x in range(0,2)]
lbaString2=["        "]
lastCommand = ''
lastCommandRW = 'false'
commandFound = 'false'
dataSearchNext=  'false'
addedPrintString = ''

interruptCount = 0
lineLength = 10
bufferData = 0
nextIndex = 0

print('Input file = ' + inputFile1)
print()
print('Output file = ' + outputFile1)
print()

#  The result of this is a file Notification.out with the notifications decoded plus the buffer start for event buffer and notification buffer.
(buffer1, buffer2) = ProcessTheNotificationAndEventBuffers(j, k, bufferData, 'Notification.out')
(base, depth) = ProcessTheCommandFIFO()
if (buffer1 > buffer2):
    eventBuffer = buffer2
    notificationBuffer = buffer1
else:
    eventBuffer = buffer1
    notificationBuffer = buffer2

j.seek(0)

commandQueues         = [0 for x in range(0, 10)]
commandQueueDepths    = [0 for x in range(0, 10)]
statusQueues          = [0 for x in range(0, 10)]
statusQueueDepths     = [0 for x in range(0, 10)]

ExtractAQueue('CommandFIFO.txt', 512, 64, commandQueues, commandQueueDepths)
ExtractAQueue('Status.txt', 512, 16, statusQueues, statusQueueDepths)

commandQueueCnt = 0
statusQueueCnt = 0

i = 0
for i in commandQueues:
    if (i != 0):
        commandQueueCnt += 1

for i in statusQueues:
    if (i != 0):
        statusQueueCnt += 1

# Make sure we have the same number of queues.  I saw an error case where I got an extra status queue.
SanityCheckTheQueues(commandQueues, commandQueueDepths, commandQueueCnt,  statusQueues, statusQueueDepths, statusQueueCnt)

commandQueueCnt = 0
statusQueueCnt = 0
i = 0

for i in commandQueues:
    if (i != 0):
        commandQueueCnt += 1

for i in statusQueues:
    if (i != 0):
        statusQueueCnt += 1

print(commandQueues)       
print(commandQueueCnt)
print(statusQueues)

print(statusQueueCnt)

 

 

 

print('Notification and Event Buffers')

print(str(hex(int(buffer1))))

print(str(hex(int(buffer2))))

 

m.write('\n\n')

 

m.write('Found   ' +  str(commandQueueCnt) + ' Command Queues \n' )

 

for i in range(0, commandQueueCnt):

    m.write(commandQueues[i] + '    ')

 

m.write('\n\n')

m.write('The queue depth may be inaccurate.  It is only correct when the trace contains a queue rollover.  \n\n')

for i in range(0, commandQueueCnt):

 

    m.write( ' Max Queue Value = ' + str(commandQueueDepths[i] + 1) + '    ')

 

m.write('\n\n')   

 

 

m.write(' Found   ' + str(statusQueueCnt) + ' Status Queues \n')

 

for i in range(0, statusQueueCnt):

    m.write(statusQueues[i]  + '    ')

 

m.write('\n\n')

m.write('The queue depth may be inaccurate.  It is only correct when the trace contains a queue rollover.  \n\n')

for i in range(0, statusQueueCnt):

    m.write( ' Max Queue Value = ' + str(statusQueueDepths[i] + 1) + '    ')

 

m.write('\n\n')

m.write('  Event Memory Base   ' + str(hex(int(buffer2))) + '        Notification Memory Base    ' +  str(hex(int(buffer1))) + '\n')

m.write('\n')

 

 

 

m.write('{:24s}'.format('Sequence #') + '{:60s}'.format('Command') + '{:20s}'.format('Time') + '{:10s}'.format('Slot') + '{:10s}'.format('Queue') + '{:10s}'.format('Status') +'\n\n\n')
ProcessCommandAndStatus(j, k, bufferData, 'Notification.out', commandQueues, commandQueueCnt, statusQueues, statusQueueCnt)

 

#  The first line is not relevent.

 

 

myVar1 = j.readline()

thisLoopCount = 0

 

 

print()

print()

print('Scanning the file for Commands. This can take 5 min. ')

 

j.seek(0)

queueInUse = 0

slot = 0

while (lineLength != 0):

#for pp in range(0,10000000):

    commandType = ''

    myVar1 = j.readline()

    thisLoopCount = thisLoopCount + 1

    if ((thisLoopCount % 1000000) == 0):

#    if ((thisLoopCount > 18000000)):

        print('Sequence #  ' + str(thisLoopCount))

    lineLength = len(myVar1)

    arrayOfCommandData[1] =''

 

    (xx, yy) = ProcessTheLine(myVar1, arrayOfCommandData, k, readArray, n, interruptCount, eventBuffer, notificationBuffer, commandQueues, commandQueueCnt, queueInUse, slot)

    queueInUse = xx

    slot = yy               

 

    if len(myVar1) == 0:

        break

 

 

j.close()

 

k.close()

n.close()

 

# Now we have the commands and status we need to pair them up.

PairStatusWithCommands('Temp.out', 'Status.txt', m)  

m.close()            

    

 

 

 

 

 

 


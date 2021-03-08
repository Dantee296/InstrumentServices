    def interpret_dtxMessgae(self, buffer: bytes, name):
        """
        Interrupt brief dtxMessage.
        """

        def illustrate_messageHeader(buf):
            """
            Interpret the content of DTXMessageHeader
            """
            print("DtXMessageHeader:")
            print("magic: ", hex(header.magic))
            print("cb: ", header.cb)
            print("fragmentId: ", header.fragmentId)
            print("fragmentCount: ", header.fragmentCount)
            print("message length: ", header.length)
            print("identifier: ", header.identifier)
            print("conversationIndex: ", header.conversationIndex)
            print("channelCode: ", header.channelCode)
            print("expectsReply: ", header.expectsReply)
            print("\n")

        def illustrate_payloadHeader(buf):
            """
            Interpret the content of DTXMessagePayload if exsits.
            """
            print("DTXMessagePayloadHeader:")
            print("flags: ", hex(payload_header.flags))
            print("auxiliaryLength: ", payload_header.auxiliaryLength)
            print("totalLength: ", payload_header.totalLength)
            print("\n")

        def illustrate_auxiliaryHeader(buf):
            """
            Interpret the header of auxiliary.
            """
            print("DTXMessageAuxiliaryHeader:")
            print("magic: ", hex(auxiliary_header.magic))
            print("length: ", auxiliary_header.length)
            print("\n")

        def illustrate_auxiliaryContent(buf):
            """
            Interpret the auxiliary content if exsits.
            """
            print("Auxiliary content:")
            print("auxiliary: ", _auxiliary)
            print("\n")

        def illustrate_selector(buf):
            """
            Interpret the content of selector.
            """
            print("Selector:")
            print("selector: ", selector)

        def check_type(buf):
            length = len(buf)
            if length >= 32:
                test_header = DTXMessageHeader.from_buffer_copy(buf[0: sizeof(DTXMessageHeader)])
                if test_header.magic == 0x1f3d5b79:
                    return "DTXMessageHeader"
                else:
                    return "DTXMessagePayloadHeader"
            else:
                test_header = DTXPayloadHeader.from_buffer_copy(buf[0: sizeof(DTXPayloadHeader)])
                if test_header.flags == 0x2 or test_header.flags == 0x3 or test_header.flags == 0x1:
                    return "DTXMessagePayloadHeader"
                elif test_header.flags == 0x0:
                    return "null"
                return "Auxiliary"

        print("______________ The content of dtxMessage in " + name)
        print("______________ Start: ")
        print("\n")
        buf = buffer
        _buf = buffer
        type_of_buf = check_type(buf)
        if type_of_buf == "Auxiliary":
            _auxiliary = auxiliary_to_pyobject(buf)
            illustrate_auxiliaryContent(_auxiliary)
            return
        elif type_of_buf == "null":
            return
        elif type_of_buf == "DTXMessagePayloadHeader":
            cur = 0
            payload_header = DTXPayloadHeader.from_buffer_copy(buf[0: sizeof(DTXPayloadHeader)])
            cur += sizeof(DTXPayloadHeader)
            illustrate_payloadHeader(payload_header)

            if payload_header.auxiliaryLength > 0:
                auxiliary_header = DTXAuxiliariesHeader.from_buffer_copy(
                    buf[cur: cur + sizeof(DTXAuxiliariesHeader)])
                cur += sizeof(DTXAuxiliariesHeader)
                illustrate_auxiliaryHeader(auxiliary_header)

                if auxiliary_header.length > 0:
                    _auxiliary = auxiliary_to_pyobject(buf[cur: cur + auxiliary_header.length])
                    cur += auxiliary_header.length
                    illustrate_auxiliaryContent(_auxiliary)

                selector = archiver.unarchive(buf[cur:])
                illustrate_selector(selector)
            return

        cursor = sizeof(DTXMessageHeader)
        header = DTXMessageHeader.from_buffer_copy(_buf[0: cursor])
        illustrate_messageHeader(header)

        if header.length > 0 and len(_buf) > 32:
            payload_header = DTXPayloadHeader.from_buffer_copy(_buf[cursor: cursor + sizeof(DTXPayloadHeader)])
            cursor += sizeof(DTXPayloadHeader)
            illustrate_payloadHeader(payload_header)

            if payload_header.auxiliaryLength > 0:
                auxiliary_header = DTXAuxiliariesHeader.from_buffer_copy(
                    _buf[cursor: cursor + sizeof(DTXAuxiliariesHeader)])
                cursor += sizeof(DTXAuxiliariesHeader)
                illustrate_auxiliaryHeader(auxiliary_header)

                if auxiliary_header.length > 0:
                    # _auxiliary = auxiliary_to_pyobject(buf[cursor: cursor + auxiliary_header.length])

                    _auxiliary = []
                    m, t = struct.unpack("<ii", _buf[cursor: cursor + 8])
                    if t == 2:
                        l, = struct.unpack("<i", _buf[cursor + 8: cursor + 12])
                        assert len(_buf[cursor: cursor + auxiliary_header.length]) == 12 + l
                        _auxiliary.append(archiver.unarchive(_buf[cursor + 12:cursor + auxiliary_header.length]))
                    elif t == 3:
                        n, = struct.unpack("<i", _buf[cursor + 8: cursor + 12])
                        _auxiliary.append(n)
                    elif t == 4:
                        n, = struct.unpack("<q", _buf[cursor + 8: cursor + 16])
                        _auxiliary.append(n)

                    cursor += auxiliary_header.length
                    illustrate_auxiliaryContent(_auxiliary)

            if header.length - payload_header.auxiliaryLength - sizeof(DTXPayloadHeader) != 0:
                selector = archiver.unarchive(_buf[cursor:])
                illustrate_selector(selector)

        print("__________ End")
        print("\n")

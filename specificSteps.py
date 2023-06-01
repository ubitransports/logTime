STEPS = [
    Step("Process support", "SmartcardNfcReader.* CARD_INSERTED", "CalypsoReaderDelegate.*processSupport: duration=",
         sub_types=[
                RepeatingStep("Contactless Reader transmit", r"ReaderImpl.*transmitApdu\(\) apduIn=", r"ReaderImpl.*transmitApdu\(\) result="),
                RepeatingStep("SAM Reader transmit", r"SamReaderImpl.*transmitApdu\(\) apduIn=", r"SamReaderImpl.*transmitApdu\(\) result=")])
]
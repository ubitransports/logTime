from repeatingstep import RepeatingStep
from step import Step

STEPS_GLOBAL = [
    Step("Process support", "SmartcardNfcReader.* CARD_INSERTED", "CalypsoReaderDelegate.*processSupport: duration=",
         sub_types=[
                RepeatingStep("Contactless Reader transmit", r"ReaderImpl.*transmitApdu\(\) apduIn=", r"ReaderImpl.*transmitApdu\(\) result="),
                RepeatingStep("SAM Reader transmit", r"SamReaderImpl.*transmitApdu\(\) apduIn=", r"SamReaderImpl.*transmitApdu\(\) result=")])
]
STEPS_V1 = [
    Step("Authentication", r"\[UTL\] Support authenticate$", r"\[UTL\] Support Authenticate result: Ok"),
    Step("Read support", r"\[UTL\] Read contactless Support$", r"\[UTL\] End read contactless Support$"),
    Step("Process support", "SmartcardNfcReader.* CARD_INSERTED", "CalypsoReaderDelegate.*processSupport: duration=",
         sub_types=[
                RepeatingStep("Contactless Reader transmit", "ReaderImpl.*transmitApdu.*apduIn", "ReaderImpl.*APDU reply"),
                RepeatingStep("SAM Reader transmit", "SamReaderImpl.*Data In", "SamReaderImpl.*Data Out")])
]
STEPS_OPTIM = [
    Step("Container selection", "getFirstMatchingCalypso", "Found a card",
         sub_types=[
                RepeatingStep("Contactless Reader transmit", r"ReaderImpl.*transmitApdu\(\) apduIn=", r"ReaderImpl.*transmitApdu\(\) result=")]),
    Step("Session open", "Opening Debit session", "Debit session open",
         sub_types=[
                RepeatingStep("Contactless Reader transmit", r"ReaderImpl.*transmitApdu\(\) apduIn=", r"ReaderImpl.*transmitApdu\(\) result="),
                RepeatingStep("SAM Reader transmit", r"SamReaderImpl.*transmitApdu\(\) apduIn=", r"SamReaderImpl.*transmitApdu\(\) result=")]),
    Step("Container environment", "Container read environment$", "Container read environment done$",
         sub_types=[
                RepeatingStep("Contactless Reader transmit", r"ReaderImpl.*transmitApdu\(\) apduIn=", r"ReaderImpl.*transmitApdu\(\) result=")]),
    Step("Authentication", "Authenticate container$", "Container Authenticated result:"),
    Step("Action list", "Start actionlist process$", "Actionlist process done$"),
    Step("Read contracts", "Read container contracts$", "Container contracts read",
         sub_types=[
                RepeatingStep("Contactless Reader transmit", r"ReaderImpl.*transmitApdu\(\) apduIn=", r"ReaderImpl.*transmitApdu\(\) result=")]),
    Step("Build card image", "Build card image$", "Card image build done$",
         sub_types=[
                RepeatingStep("Contactless Reader transmit", r"ReaderImpl.*transmitApdu\(\) apduIn=", r"ReaderImpl.*transmitApdu\(\) result=")]),
    Step("Session close", "Closing Debit session", "Debit session closed",
         sub_types=[
                RepeatingStep("Contactless Reader transmit", r"ReaderImpl.*transmitApdu\(\) apduIn=", r"ReaderImpl.*transmitApdu\(\) result="),
                RepeatingStep("SAM Reader transmit", r"SamReaderImpl.*transmitApdu\(\) apduIn=", r"SamReaderImpl.*transmitApdu\(\) result=")]),
    Step("Process container", "Process container$", "Process container done$"),
    Step("Process support", "SmartcardNfcReader.* CARD_INSERTED", "CalypsoReaderDelegate.*processSupport: duration=",
         sub_types=[
                RepeatingStep("Contactless Reader transmit", r"ReaderImpl.*transmitApdu\(\) apduIn=", r"ReaderImpl.*transmitApdu\(\) result="),
                RepeatingStep("SAM Reader transmit", r"SamReaderImpl.*transmitApdu\(\) apduIn=", r"SamReaderImpl.*transmitApdu\(\) result=")])
]
STEPS_LIST = {"STEPS_GLOBAL": STEPS_GLOBAL, "STEPS_V1": STEPS_V1, "STEPS_OPTIM": STEPS_OPTIM}

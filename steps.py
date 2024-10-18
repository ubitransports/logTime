import copy

from repeatingstep import RepeatingStep
from step import Step

contactless = RepeatingStep("Contactless Reader transmit", r"(FlowbirdA1000Contactless|FamocoAsk|Bluebird|M2TContactless|TelpoTech|TelpoNfc)Reader.*transmitApdu.*apduIn", r"Reader.*transmitApdu.*result=")
sam = RepeatingStep("SAM Reader transmit", r"SamReader.*transmitApdu.*apduIn", r"SamReader.*transmitApdu.*result=")

STEPS_GLOBAL = [
    Step("Process support", "SmartcardNfcReader.* CARD_INSERTED", "CalypsoReaderDelegate.*processSupport: duration=",
         sub_types=[
                RepeatingStep("Contactless Reader transmit", r"(FlowbirdA1000Contactless|FamocoAsk|Bluebird)ReaderImpl.*transmitApdu.*apduIn=", r"ReaderAdapter.*transmitApdu.*result="),
                RepeatingStep("SAM Reader transmit", r"SamReaderImpl.*transmitApdu.*apduIn=", r"SamReaderImpl.*transmitApdu.*result=")])
]
STEPS_V1 = [
    #Step("Authentication", r"\[UTL\] Support authenticate$", r"\[UTL\] Support Authenticate result: Ok"),
    #Step("Read support", r"\[UTL\] Read contactless Support$", r"\[UTL\] End read contactless Support$"),
    Step("Process support", "SmartcardNfcReader.* CARD_INSERTED", "CalypsoReaderDelegate.*processSupport: duration=",
         sub_types=[
                RepeatingStep("Contactless Reader transmit", "ReaderImpl.*transmitApdu.*apduIn", "ReaderImpl.*transmitApdu.*res"),
                RepeatingStep("SAM Reader transmit", "SamReaderImpl.*apduIn", "SamReaderImpl.*res")])
]
STEPS_V2 = [
    Step("Container selection", "getFirstMatchingCalypso", "Found a card", sub_types=[copy.deepcopy(contactless)]),
    Step("Session open", "Opening Debit session", "Debit session open",
         sub_types=[
                copy.deepcopy(contactless),
                copy.deepcopy(sam)]),
    Step("Container environment", "Container read environment$", "Container read environment done$"),
    Step("Authentication", "Authenticate container$", "Container Authenticated result:"),
    Step("Action list", "Start actionlist process$", "Actionlist process done$"),
    Step("Read contracts", "Read container contracts$", "Container contracts read",
         sub_types=[
                copy.deepcopy(contactless)]),
    Step("Build card image", "Build card image$", "Card image build done$",
         sub_types=[
                copy.deepcopy(contactless)]),
    Step("Session close", "Closing Debit session", "Debit session closed",
         sub_types=[
                copy.deepcopy(contactless),
                copy.deepcopy(sam)]),
    Step("Process container", "Process container$", "Process container done$"),
    Step("Process support", "SmartcardNfcReader.* CARD_INSERTED", "CalypsoReaderDelegate.*processSupport: duration=",
         sub_types=[
                copy.deepcopy(contactless),
                copy.deepcopy(sam)])
]

STEPS_V3 = [
    Step("Container selection", "Event CARD_INSERTED received", "Successfully built intercode container",
         sub_types=[
                copy.deepcopy(contactless)]),
    Step("Session open", "Opening Debit session", "Debit session open",
         sub_types=[
                copy.deepcopy(contactless),
                copy.deepcopy(sam)]),
    Step("Container build environment", "Container read environment$", "Container read environment done$"),
    Step("Identification", "Identify container$", "Container identified result:"),
    Step("Action list", "Start distribute process$", "Distribute process done$"),
    Step("Read contracts", "Read container contracts$", "Container contracts read",
         sub_types=[
                copy.deepcopy(contactless)]),
    Step("Build card image", "Build card image$", "Card image build done$"),
    Step("Consume contract", "Consume started for contract", "Consume operation done.$",
         sub_types=[
                copy.deepcopy(contactless),
                copy.deepcopy(sam)]),
    Step("Process support", "Event CARD_INSERTED received", "Consume operation done.$",
         sub_types=[
                copy.deepcopy(contactless),
                copy.deepcopy(sam)])
]
STEPS_LIST = {"STEPS_GLOBAL": STEPS_GLOBAL, "STEPS_V1": STEPS_V1, "STEPS_V2": STEPS_V2, "STEPS_V3": STEPS_V3}

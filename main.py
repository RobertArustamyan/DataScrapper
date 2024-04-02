from Functions.converting_to_excel import converter
from Functions.geting_data_from_link import GettingData
from Functions.links_parsing import FindingSellParseItemLinks, FindingRentParseItemLinks

if __name__ == "__main__":
    SellItemLinks = FindingSellParseItemLinks()
    RentItemLinks = FindingRentParseItemLinks()

    # Finding links to parse
    SellItemLinks.get_data_links('SellLinks')
    RentItemLinks.get_data_links('RentLinks')

    # Parsing links
    parser = GettingData()
    parser.start_parse()

    # Convert .csv to .xlsx
    converter()

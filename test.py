from main import top_ten_pairs

def test_url():
    url = 'https://www.icicibank.com/Personal-Banking/insta-banking/internet-banking/index.page'
    result = top_ten_pairs(url)
    expected_pairs = [('Know More', 960), ('Apply Now', 551), ('Credit Card', 327), ('and more', 280), ('Savings Account', 234), ('ICICI Bank', 121), ('Forex Prepaid', 120), ('Prepaid Card', 115), ('Fixed Deposit', 107)]
    expected_words = [('More', 1181), ('Know', 1010), ('Card', 634), ('Now', 616), ('and', 604), ('Apply', 571), ('Loan', 466), ('Credit', 419), ('your', 360)]
    assert len(result) == 2
    assert len(result[0]) == 9
    assert len(result[1]) == 9
    assert result[0] == expected_pairs
    assert result[1] == expected_words

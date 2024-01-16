import unittest   

class Lobbyist:
    def __init__(self, lobbyist_id, lobbyist_lastname, lobbyist_firstname, lobbyist_address1, lobbyist_address2, lobbyist_city, lobbyist_state, lobbyist_zip, income, lobbyistactivities):
        self.lobbyist_id = lobbyist_id
        self.lobbyist_lastname = lobbyist_lastname
        self.lobbyist_firstname = lobbyist_firstname
        self.lobbyist_address1 = lobbyist_address1
        self.lobbyist_address2 = lobbyist_address2
        self.lobbyist_city = lobbyist_city
        self.lobbyist_state = lobbyist_state
        self.lobbyist_zip = lobbyist_zip
        self.income = {2000}
        self.lobbyistactivities = []
    def add_income(self, date_income_received, income_amount):
        self.income[date_income_received] = income_amount
    def __str__(self):        
        return f'{self.lobbyist_id}{self.lobbyist_lastname}{self.lobbyist_firstname}'
    def total_income(self):
        return sum(self.income)
    def add_LobbyistActivities(self, LobbyistActivities):
        self.lobbyistactivities.append(LobbyistActivities)
class LobbyistActiviy:
    def __init__(self, lobbyist_id, client_name, income_amount, date_income_received):
        self.lobbyist_id = lobbyist_id
        self.client_name = client_name
        self.income_amount = income_amount
        self.date_income_received = date_income_received    

class TestLobbyist(unittest.TestCase):
    def setUp(self):
        self.lobbyist = Lobbyist("McKee", "Nancy", "225 Manchester Drive", " ", "Zionsville", "IN", "46077", "20185033599", "2000", " ")
    # Test the canculate method
    def test_total_income(self):
        self.assertEqual(self.lobbyist.total_income(),2000)
    # Test the str method
    def test_str(self):
        self.assertEqual(str(self.lobbyist), "McKeeNancy225 Manchester Drive")
        print(self.lobbyist)  
        
if __name__ == '__main__':
    unittest.main()
        

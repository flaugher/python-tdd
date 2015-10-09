from pdb import set_trace as debug
from selenium import webdriver
import unittest

# First example of a functional test

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        # User goes to homepage of a to-do web app
        self.browser.get('http://localhost:8000')

        # User notices page title and header mentioning to-do list
        self.assertIn('To-Do', self.browser.title)
        self.fail("Finish the test!")

        # User invited to enter a to-do item

        # User types "Buy peacock feathers"

        # When user hits enter, the page updates and now page lists
        # "1: Buy peacock feathers" as a to-do item

        # There is still a textbox inviting her to add another item.
        # User enters "Use peacock features to make a fly"

        # The page updates again and shows both to-do items

        # User notices site has generated a unique URL for her

        # User visits that URL and to-do list is still there

        # User finishes

if __name__ == '__main__':
    unittest.main()

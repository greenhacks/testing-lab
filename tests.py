"""Testsq for Balloonicorn's Flask app."""

import unittest 
import party

class PartyTests(unittest.TestCase):
    """Tests for my party site."""

    def setUp(self):
        """Code to run before every test."""

        self.client = party.app.test_client()
        party.app.config['TESTING'] = True

    def test_homepage(self):
        """Can we reach the homepage?"""

        result = self.client.get("/")
        self.assertIn(b"having a party", result.data)

    def test_no_rsvp_yet(self):
        """Do users who haven't RSVPed see the correct view?"""

        # # FIXME: Add a test to show we haven't RSVP'd yet
        # print("FIXME")
        
        rsvp_info = {'name': "", 'email': ""}

        result = self.client.post("/rsvp", data=rsvp_info)

        # users are only supposed to see the homepage if they haven't rsvp'ed.
        # if user has rsvp'ed, they should see "Party Details
        # result = self.client.get('/rsvp')
        self.assertNotIn(b"Party Details", result.data)

    def test_rsvp(self):
        """Do RSVPed users see the correct view?"""

        rsvp_info = {'name': "Jane", 'email': "jane@jane.com"}

        result = self.client.post("/rsvp", data=rsvp_info,
                                  follow_redirects=True)

        # FIXME: check that once we log in we see party details--but not the form!
        
        self.assertIn(b"Party Details", result.data)
        self.assertNotIn(b"Please RSVP", result.data)

        # print("FIXME")

    def test_rsvp_mel(self):
        """Can we keep Mel out?"""

        # FIXME: write a test that mel can't invite himself

        result = self.client.post("/rsvp", data={'name': 'Mel Melipolski', 'email': 'mel@ubermelon.com'},
                                    follow_redirects=True)
        self.assertNotIn(b"Treats", result.data)
        # pass
        # print("FIXME")


if __name__ == "__main__":
    unittest.main()

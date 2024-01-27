from unittest import TestCase
from app import app
from flask import session
from boggle import Boggle


class FlaskTests(TestCase):

    def setUp(self):
        self.client = app.test_client()
        app.config['TESTING'] = True
    
    def test_board(self):
        with self.client:
            response = self.client.get('/')
            self.assertIn('board', session)
            self.assertIn('score', response.data)
            self.assertIsNone(session.get('highscore'))
            self.assertIsNone(session.get('nplays'))

    def test_valid_word(self):

        with self.client as client:
            with client.session_transaction() as sess:
                sess['board'] = [["R","U","N","D","E"],
                                 ["R","U","N","D","E"],
                                 ["R","U","N","D","E"],
                                 ["R","U","N","D","E"],
                                 ["R","U","N","D","E"]]
        response = self.client.get('/words_check?word=run')
        self.assertEqual(response.json['result'], 'ok')

    def not_word(self):

        self.client.get('/')
        response = self.client.get('/words_check?word=notaword')
        self.assertEqual(response.json['result'], 'not a word')

  

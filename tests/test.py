import unittest
from app import Phonebook

class TestPhonebook(unittest.TestCase):
    def setUp(self):
        self.contacts = Phonebook()

    def test_add_contacts(self):
        value = self.contacts.add_contacts('benedict',123, 'r@gmail.com')

        results= value["name"] in self.contacts.details


        self.assertEqual(results, True )

        #test if it raises an exeption when contact exist


    def test_update_contacts(self):
        #add a contact
        self.contacts.add_contacts("tunchi", 456, 'y@gmail')

        #update a contact
        self.contacts.update_contacts("tunchi", 678, 's@gmail' )

        self.assertEqual(self.contacts.details['tunchi'], {"name":"tunchi", "contacts":678, "email":"s@gmail"})


    def test_delete_contact(self):
         self.contacts.add_contacts("vybz", 456, 'tyy')

         results = self.contacts.delete_contacts("vybz")




         self.assertEqual(results, {})

    def test_view_all_contact(self):
        self.contacts.add_contacts("steve", 456, 'y@gmail')
        self.contacts.add_contacts("tunchi", 456, 'y@gmail')
        self.contacts.add_contacts("tessy", 456, 'y@gmail')
        self.contacts.add_contacts("tom", 456, 'y@gmail')
        results = self.contacts.view_all_contacts()

        self.assertEqual(results, {'steve': {'contacts': 456, 'email': 'y@gmail', 'name': 'steve'},
 'tom': {'contacts': 456, 'email': 'y@gmail', 'name': 'tom'},
 'tessy': {'contacts': 456, 'email': 'y@gmail', 'name': 'tessy'},
 'tunchi': {'contacts': 456, 'email': 'y@gmail', 'name': 'tunchi'}})




if __name__ == '__main__':
    unittest.main()

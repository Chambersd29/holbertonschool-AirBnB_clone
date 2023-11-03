#!/usr/bin/python3
"""
Este modulo contiene los casos de prueba para
nuestra clase BaseModel.
"""


import unittest

from models.base_model import BaseModel
import time


class TestBaseModel(unittest.TestCase):
    """
    Esta clase define los casos de prueba.
    """

    def setUp(self):
        """
        Se crea una instancia de nuestra clase BaseModel
        """
        self.bm = BaseModel()

    def test_init(self):
        """
        Se comparan los atributos con los tipos de datos.
        """
        self.assertIsInstance(self.bm.id, str)

    def test_return(self):
        """
        Compara el retorno como None de save().
        """
        self.assertIsNone(self.bm.save())

    def test_compare_attrs(self):
        """
        Verifica que contengan todos los atributos.
        """
        model_dict = self.bm.to_dict()
        self.assertIn('id', model_dict)
        self.assertIn('created_at', model_dict)
        self.assertIn('updated_at', model_dict)
        self.assertIn('__class__', model_dict)

    def test_methods_magic_str(self):
        """
        Compara la salida del método magic __str__.
        """
        bm = BaseModel()
        expected_output = "[{}] ({}) {}".format(
            bm.__class__.__name__, bm.id, bm.__dict__)
        self.assertEqual(str(bm), expected_output)

    def test_update_date(self):
        """
        Este test actualiza el atributo updated_at, para compararlo
        después de llamar al método save().
        """
        model = BaseModel()
        original_updated_at = model.updated_at
        original_created_at = model.created_at
        time.sleep(1)
        model.save()
        self.assertNotEqual(original_updated_at, model.updated_at)
        self.assertTrue(original_created_at, model.created_at)
        self.assertNotEqual(model.updated_at, model.created_at)

    def test_save(self):
        model = BaseModel()
        self.assertIsNone(model.save())


if __name__ == "__main__":
    unittest.main()

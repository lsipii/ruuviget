import os
from dotenv import load_dotenv

load_dotenv()

from app.utils.data_structures import singleton
from app.utils.value_parsers import ensure_type, parse_boolean, parse_comma_separated_text_list, parse_tuple


@singleton
class Settings:
    def get_list(self, setting_name: str, list_item_type=None, convert_to_item_type=False, default_value=None):
        """
        Gets a list type setting
        """
        list_items = self.get_setting(setting_name, None)
        if list_items is not None:
            if isinstance(list_items, list):
                parts = list_items
                parts = self.__prepare_list(parts, list_item_type, convert_to_item_type)
                return parts
            elif isinstance(list_items, str):
                parts = parse_comma_separated_text_list(list_items)
                parts = self.__prepare_list(parts, list_item_type, convert_to_item_type)
                return parts
        return default_value

    def get_tuple(self, setting_name: str, default_value=None) -> tuple:
        """
        Gets a tuple
        """
        tuple_value = self.get_setting(setting_name)
        if tuple_value is not None:
            return parse_tuple(tuple_value, default_value)
        return default_value

    def get_boolean(self, setting_name: str) -> bool:
        """
        Gets a boolean type setting
        """
        true_value = self.get_setting(setting_name, None)
        if true_value is not None:
            return parse_boolean(true_value)
        return False

    def get_setting(self, setting_name, default_value=""):
        """
        Gets a setting from env values
        """
        return os.getenv(setting_name, default_value)

    def set_setting(self, settingName, value):
        """
        Sets a setting
        """
        os.environ[settingName] = str(value)

    def __prepare_list(self, list_items: list, list_item_type=None, convert_to_item_type=False) -> list:
        if list_item_type is not None:
            for index, list_item in enumerate(list_items):
                if not isinstance(list_item, list_item_type):
                    if convert_to_item_type:
                        list_items[index] = ensure_type(list_item, list_item_type)
                    else:
                        raise Exception("Bad list input")

        return list_items

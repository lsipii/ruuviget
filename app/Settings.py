import os
from dotenv import load_dotenv

load_dotenv()

from app.data_structures import parse_comma_separated_text_list, singleton


@singleton
class Settings:
    def get_list(self, setting_name: str, list_item_type=None):
        list_items = self.get_setting(setting_name, None)
        if list_items is not None:
            if isinstance(list_items, list):
                parts = list_items
                self.__validate_list(parts, list_item_type)
                return parts
            elif isinstance(list_items, str) and list_items.find(",") > -1:
                parts = parse_comma_separated_text_list(list_items)
                self.__validate_list(parts, list_item_type)
                return parts
        return None

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

    def __validate_list(self, list_items, list_item_type=None):
        if list_item_type is not None:
            for list_item in list_items:
                if not isinstance(list_item, list_item_type):
                    raise Exception("Bad list input")

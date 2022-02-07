from properties.validation.property_error import PropertyError


class PropertiesValidator:
    @staticmethod
    def validate_property_non_none(property):
        if property is None:
            raise PropertyError("Property is None. The set method need to be called prior to accessing any property.")

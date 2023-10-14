from django.core.files.storage import Storage
# Storage.
import os

class AlwaysOverwriteFileSystemStorage(Storage):
    def get_available_name(self, name):
        """
        Directly Returns a filename that's
        from what user input.
        """
        if self.exists(name):
    # Remove the existing file
            os.remove(name)
    # Return the input name as output
        return name
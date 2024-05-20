from src.requester import requester
from requests.exceptions import HTTPError

class Items:
    def search(self, url, header, params):
        """
        This function was built for searching details on your favorite animes.
        
        Args:
            header (dict): a dict containing the access token, e.g., {'Authorization: f"Bearer {access_token}"'}
            params (dict): a dict containing the parameters of the query like: q, limit, fields, etc...

        Returns:
            items (dict): a dict containing myanimelist data
        """

        try:
            response = requester.get(url, header, params)
            response.raise_for_status()
            items = response.json()
        except HTTPError as e:
            raise e

        print('All went well!')
        
        return items
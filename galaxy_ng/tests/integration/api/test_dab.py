import pytest
from ..utils import get_client

from ansible.galaxy.api import GalaxyError


@pytest.mark.min_hub_version("4.10dev")
@pytest.mark.all
@pytest.mark.deployment_community
def test_dab_service_index_is_not_available(ansible_config):

    config = ansible_config("admin")
    api_prefix = config.get("api_prefix").rstrip("/")
    api_client = get_client(config, request_token=True, require_auth=True)

    url = api_prefix + '/service-index/'
    with pytest.raises(GalaxyError) as e:
        api_client.request(url)

    assert 'HTTP Code: 404, Message: Not Found' in str(e.value)

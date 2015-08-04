require 'serverspec'

describe user('till') do
  it { should exist }
  it { should have_authorized_key 'ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAAAgQCfO2TgNUMcY9K8N9SsAU/LfVtlloO50n6NRxDER8dCi+t1ydalTbNdEj52cIjqvIEn458cCxdCwsNYeWqSVggX7vT7a+DgYZlJcRteHcb0lPYZplPuiZe3AUE9rHH48W4xEopv7J8Wz6hLng6Gb0TQx9HeVybQ5dn6CGyt8sOCKQ== Fritz Brinkhoffs' }
  it { should belong_to_group 'sudo' }
end
# frozen_string_literal: true

describe file('/usr/local/bin/greenbay') do
  it { should exist }
end

describe command('greenbay --version') do
  its('stdout') { should eq "greenbay version 0.0.1-pre\n" }
end

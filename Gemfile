source "https://rubygems.org"

gemspec

# mime-types 3+, required by mail, requires ruby 2.0+
gem "mime-types", "< 3" if Gem::Version.new(RUBY_VERSION) < Gem::Version.new("2")

#group :development do
#  gem "pry"
#end

# エラーが出るため追加した
# https://stackoverflow.com/questions/45269621/phusion-error-undefined-method-has-for-sassutilmodule
gem 'compass-rails', git: 'git@github.com:Compass/compass-rails.git'

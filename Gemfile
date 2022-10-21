source 'https://rubygems.org'
git_source(:github) { |repo| 'https://github.com/#{repo}.git' }

# Ruby 2.7.4 https://www.ruby-lang.org/en/news/2021/07/07/ruby-2-7-4-released/
ruby '2.7.4'

# Bundle edge Rails instead: gem 'rails', github: 'rails/rails', branch: 'main'
gem 'rails', '~> 7.0.4'

# The original asset pipeline for Rails [https://github.com/rails/sprockets-rails]
gem 'sprockets-rails'
# Use sqlite3 as the database for Active Record [https://github.com/sparklemotion/sqlite3-ruby]
gem 'sqlite3'
# Use the Puma web server [https://github.com/puma/puma]
gem 'puma', '~> 5.0'
# Use JavaScript with ESM import maps [https://github.com/rails/importmap-rails]
gem 'importmap-rails'
# Hotwire's SPA-like page accelerator [https://turbo.hotwired.dev]
gem 'turbo-rails'
# Hotwire's modest JavaScript framework [https://stimulus.hotwired.dev]
gem 'stimulus-rails'
# Reduces boot times through caching; required in config/boot.rb [https://github.com/Shopify/bootsnap]
gem 'bootsnap', require: false
# Get rid of warnings: https://stackoverflow.com/questions/67773514/
gem "net-http"

group :development, :test do
  # RSpec testing framework to Ruby on Rails as alternative to its default testing framework
  # Adding it to the :development group is not strictly necessary, but without it, generators and rake tasks must be preceded by RAILS_ENV=test
  # rspec-rails 6.x for Rails 6.1 or 7.x [https://github.com/rspec/rspec-rails]
  gem 'rspec-rails', '~> 6.0.0'
  # State of the art fixtures [https://github.com/thoughtbot/factory_bot_rails]
  # See https://guides.rubyonrails.org/debugging_rails_applications.html#debugging-with-the-debug-gem
  gem 'debug', platforms: %i[ mri mingw x64_mingw ]
end

group :development do
  # Access an interactive console on exception pages or by calling 'console' (<%= console %>) anywhere in the code.
  gem 'web-console' # [https://github.com/rails/web-console]
end

group :test do
  # Use system testing [https://guides.rubyonrails.org/testing.html#system-testing]
  # Test web applications by simulating how a real user would interact with your app [https://github.com/teamcapybara/capybara]
  gem 'capybara'
  gem 'selenium-webdriver'
  gem 'webdrivers'
  gem 'factory_bot_rails'
end

# Windows does not include zoneinfo files, so bundle the tzinfo-data gem
gem 'tzinfo-data', platforms: [:mingw, :mswin, :x64_mingw, :jruby]

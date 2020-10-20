source 'https://rubygems.org'
git_source(:github) { |repo| "https://github.com/#{repo}.git" }

ruby '2.7.2'

# Bundle edge Rails instead: gem 'rails', github: 'rails/rails'
gem 'rails', '~> 6.0.3', '>= 6.0.3.4'
# Use sqlite3 as the database for Active Record
gem 'sqlite3', '~> 1.4' # https://www.sqlite.org/index.html
# Use Puma as the app server
gem 'puma', '~> 5.0', '>= 5.0.2' # https://github.com/puma/puma
# Transpile app-like JavaScript, Webpacker is the default JavaScript compiler for Rails 6
gem 'webpacker', '~> 4.0' # https://github.com/rails/webpacker
# Turbolinks makes navigating your web application faster
# When you follow a link, Turbolinks automatically fetches the page, swaps in its <body>, and merges its <head>
gem 'turbolinks', '~> 5' # https://github.com/turbolinks/turbolinks
# Build JSON APIs with ease. Read more: https://github.com/rails/jbuilder
# gem 'jbuilder', '~> 2.7'
# Use Redis adapter to run Action Cable in production
# gem 'redis', '~> 4.0'

# Reduces boot times through caching; required in config/boot.rb
gem 'bootsnap', '>= 1.4.2', require: false # https://github.com/Shopify/bootsnap

group :development, :test do
  # Call 'byebug' anywhere in the code to stop execution and get a debugger console
  gem 'byebug', platforms: [:mri, :mingw, :x64_mingw], platforms: [:mri, :mingw, :x64_mingw] # https://github.com/deivid-rodriguez/byebug
  # RSpec testing framework as a drop-in alternative to Rails' default testing framework, Minitest
  gem 'rspec-rails', '~> 4.0', '>= 4.0.1' # https://github.com/rspec/rspec-rails
  # State of the art fixtures
  gem 'factory_bot_rails', '~> 6.1' # https://github.com/thoughtbot/factory_bot_rails
  # Capybara: Test web applications by simulating how a real user would interact with your app
  gem 'capybara', '~> 3.33' # https://github.com/teamcapybara/capybara/blob/3.33_stable/README.md#using-capybara-with-rspec
  # Access an interactive console on exception pages or by calling 'console' (<%= console %>) anywhere in the code.
  gem 'web-console', '>= 3.3.0'
  gem 'listen'
end

# Windows does not include zoneinfo files, so bundle the tzinfo-data gem
gem 'tzinfo-data', platforms: [:mingw, :mswin, :x64_mingw, :jruby]

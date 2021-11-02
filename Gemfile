source 'https://rubygems.org'
git_source(:github) { |repo| "https://github.com/#{repo}.git" }

# Ruby 2.7.4 https://www.ruby-lang.org/en/news/2021/07/07/ruby-2-7-4-released/
ruby '2.7.4'

# Bundle edge Rails instead: gem 'rails', github: 'rails/rails'
gem 'rails', '~> 6.0.3', '>= 6.0.3.4' # https://github.com/rails/rails
# Use sqlite3 as the database for Active Record
gem 'sqlite3' # https://github.com/sparklemotion/sqlite3-ruby
# Use Puma as the app server
gem 'puma', '~> 5.0', '>= 5.0.2' # https://github.com/puma/puma
# Minimal, modern embedded V8 for Ruby
# See https://github.com/rails/execjs#readme for more supported runtimes
gem 'mini_racer', platforms: :ruby # https://github.com/rubyjs/mini_racer
# Reduces boot times through caching; required in config/boot.rb
gem 'bootsnap', '>= 1.1.0', require: false # https://github.com/Shopify/bootsnap
# Turbolinks makes navigating your web application faster
gem 'turbolinks', '~> 5' # https://github.com/turbolinks/turbolinks

group :development, :test do
  # Call 'byebug' anywhere in the code to stop execution and get a debugger console
  gem 'byebug', platforms: [:mri, :mingw, :x64_mingw]
  # Rails 6 needs at least version 4.0: https://github.com/rspec/rspec-rails/issues/2177
  gem 'rspec-rails', '>= 4.0' # https://github.com/rspec/rspec-rails
  # Adds support for Capybara system testing and selenium driver
  gem 'capybara', '>= 2.15'
  # State of the art fixtures
  gem 'factory_bot_rails', '~> 6.1' # https://github.com/thoughtbot/factory_bot_rails
end

group :development do
  gem 'listen', '>= 3.0.5', '< 3.2'
  # Access an interactive console on exception pages or by calling 'console' (<%= console %>) anywhere in the code.
  gem 'web-console', '>= 3.3.0'
end

# Windows does not include zoneinfo files, so bundle the tzinfo-data gem
gem 'tzinfo-data', platforms: [:mingw, :mswin, :x64_mingw, :jruby]

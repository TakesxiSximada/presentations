defmodule Testing do
  def testing do
    require IEx; IEx.pry
    IO.puts "one"
    IO.puts "two"
    IO.puts "three"
    1 + 1
  end
end

Testing.testing

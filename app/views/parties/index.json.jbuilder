json.array!(@parties) do |party|
  json.extract! party, :id, :name, :owner, :time, :location, :description, :participants
  json.url party_url(party, format: :json)
end

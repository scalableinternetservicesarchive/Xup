json.array!(@join_members) do |join_member|
  json.extract! join_member, :id, :user_id, :party_id
  json.url join_member_url(join_member, format: :json)
end

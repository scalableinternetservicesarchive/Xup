open("user.txt") do |users|
    users.read.each_line do |user|
        name, email, ps, psconfirm = user.chomp.split("|")
        p name, email, ps, psconfirm
    end
end

function countValidWords(sentence::String)::Int64
    lower = "abcdefghijklmnopqrstuvwxyz"
    upper = uppercase(lower)
    digits = "0123456789"
    puncs = Set(['!', ',', '.'])
    valids = 0

    for word in split(sentence)
        if count(i->i=='-', word) > 1
            continue
        end

        if !iszero(length(intersect(Set(word), digits)))
            continue
        end

        if count(i->i in puncs, word) > 1
            continue
        end

        if '!' in word || '.' in word || ',' in word
            if !(word[end] in puncs)
                continue
            end
        end

        good = true
        for (ind, e) in enumerate(word)
            if e in upper
                good = false
                break
            end

            if e == '-'
                if ind == 1 || ind == length(word)
                    good = false
                    break
                end

                if !(word[ind-1] in lower) || !(word[ind+1] in lower)
                    good = false
                    break
                end
            end
        end

        if !good
            continue
        end

        valids += 1
    end
    return valids
end

cases = [
    ("cat and  dog", 3),
    ("!this  1-s b8d!", 0),
    ("alice and  bob are playing stone-game10", 5),
    ("he bought 2 pencils, 3 erasers, and 1  pencil-sharpener.", 6),
    ("a-b-c", 0),
    (". ! 7hk  al6 l! aon49esj35la k3 7u2tkh  7i9y5  !jyylhppd et v- h!ogsouv 5", 4),
]

for (sentence, exp) in cases
    got = countValidWords(sentence)
    @assert got == exp "Failed case ($(sentence)) - expecting ($(exp)), got ($(got))."
end

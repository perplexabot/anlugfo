function toGoatLatin(sentence::String)::String
    gl = []
    for (ind, word) in enumerate(split(sentence))
        if lowercase(word[1]) in Set(['a', 'e', 'i', 'o', 'u'])
            w = word * "ma"
        else
            w = word[2:end] * word[1] * "ma"
        end
        w = w * ('a' ^ ind)
        push!(gl, w)
    end
    return join(gl, ' ')
end

cases = [
    ("I speak Goat Latin", "Imaa peaksmaaa oatGmaaaa atinLmaaaaa"),
    (
        "The quick brown fox jumped over the lazy dog",
        "heTmaa uickqmaaa rownbmaaaa oxfmaaaaa umpedjmaaaaaa overmaaaaaaa hetmaaaaaaaa azylmaaaaaaaaa ogdmaaaaaaaaaa",
    ),
    ("I", "Imaa"),
    ("B", "Bmaa"),
]

for (sentence, exp) in cases
    got = toGoatLatin(sentence)
    @assert got == exp "Failed case ($(sentence)) - \nexpecting ($(exp))\ngot       ($(got))."
end

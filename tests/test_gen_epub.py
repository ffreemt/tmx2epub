""" test gen_epub. """

from tmx2epub.gen_epub import gen_epub


def test_gen_epub2():
    """ test_gen_epub2. """
    from pathlib import Path
    infile = r"tests\2.tmx"
    stem = Path(infile).absolute().stem
    outfile = f"{Path(infile).absolute().parent / stem}.epub"
    assert gen_epub(infile, debug=True) == outfile

    # assert 0

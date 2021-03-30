cipher = """
Give novelist and sometime art critic John Updike credit. The 2008 National Endowment for the Humanities Jefferson Lecturer tried to answer the thorny question: "What is American about American art?"
Onstage at the Warner Theatre Thursday night, in front of 1,900 culture lovers, the angular, silver-haired Updike used more than 60 images, ranging from formal mid-18th-century portraits by Bostonian John Singleton Copley to the hyper-realistic late-20th-century renderings of Richard Estes, to make his point: "The American artist . . . born into a continent without museums and art schools, took nature as his only instructor, and things as his principal study."
One of the salient traits of this country, he told the gathering, is an urge to define what is American. To delineate the romantic wildness of our nature. To search for a national self-image. That desire to map the New World is reflected in the tight classicist tradition of American art.
Drawing rules in this country's artwork, Updike said. He quoted a European-trained artist who criticized Copley -- the first American to exhibit a painting in Europe -- for being too "liney." That is, too reliant on the drawing in his paintings and not free enough with color and light.
By tracing that harsh "lineyness" in American painting, and juxtaposing it against a freer, more colorful romantic "painterliness" in other work, Updike laid out a convincing answer to his overarching what-is-American question.
Yet he did it subtly. Flashing slides of well-knowns, such as Gilbert Stuart, Winslow Homer, Grant Wood and Norman Rockwell, Updike pointed out the distinctions.
European-influenced artists, such as Homer and John Singer Sargent, tended toward the painterly; more purely American artists, such as Copley and Thomas Hart Benton, toward the liney.
Reading from a text, Updike, 76, spoke in a raspy voice. The presentation moved quickly. An invitation to deliver the Jefferson Lecture is the loftiest award given by the federal government for "distinguished intellectual achievement in the humanities," and there was a patriotic air to the affair.
Even the U.S. Marine Band showed up to play before the ceremony.
At no point during the speech did Updike, or the slideshow technology, falter. The address was based on "Picturing America," an NEH initiative to distribute reproductions of American paintings to schools and libraries.
Diversity was nearly absent in Updike's presentation. The painters he referred to were mostly males of European descent, a cohort he referred to as "that least hip of demographic groups." He did not, for instance, mention the extraordinary American painter Mary Cassatt, who became an expatriate.
Either ignored or overlooked, as well, was any reference to a 19th-century European debate -- similar to the liney-painterly dichotomy -- between classicist Jean Auguste Dominique Ingres and romanticist Eugène Delacroix.
Regardless, Updike's lecture was high-minded and provocative -- like most of his work.
Soon after the talk ended, the patrons repaired to the Willard Hotel for a wine-and-sweets reception. So did Updike.
"""

for line in [x for x in cipher.split('\n') if x]:
    print(line[0], end='')

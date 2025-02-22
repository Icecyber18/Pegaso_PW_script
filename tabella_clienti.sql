
CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(255) NOT NULL,
    cognome VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL,
    telefono INT NOT NULL,
    password_hash_(sha256) VARCHAR(255) NOT NULL,
    password_hash_(sha512) VARCHAR(255) NOT NULL
);


INSERT INTO users (nome, cognome, email, telefono, password_hash_(sha256), password_hash_(sha512))
VALUES ('Orazio', 'Tremonti', 'orazio.tremonti@tele2.it', 393801125781, '380c36f2385a93af59ec32e8cec3a00da0c9d4dea8e1c8c20d8a5abc6ff7c799', 'f5ba3e3a2345d86cff83bb9eb292ff432a98ed996666b87188088a1bb42808474af9de17a88c6075a3975d0ac8c2eb1765c711bc2e66754230560c123f34f566');

INSERT INTO users (nome, cognome, email, telefono, password_hash_(sha256), password_hash_(sha512))
VALUES ('Antonia', 'Pagliaro', 'antonia.pagliaro@tim.it', 393703086841, '73b1cfb1a918961d2498dfa32ff23e030f9306d320b9be267f24dde7ab7c5d85', '68823ced7de5290ffacc50d2fbd7132f68262e9ee77697423bfa4aef89ac7b4c2057f68fa0bc415a5ef3ed075932d892cd0a27beae0a527b6619d6c751dd95df');

INSERT INTO users (nome, cognome, email, telefono, password_hash_(sha256), password_hash_(sha512))
VALUES ('Aria', 'Togliatti', 'aria.togliatti@tin.it', 393605707925, 'b98c30dda77323ffccfe731a8e4c12437c87dc22e60437d24d2a5ab0ab11ab75', '5132095934b178d4a17cf5fededb3a9a5b1d7bb36def9eec176ba7b3c12f877bf1caeff3024fc64e5f04937ca5109a49faf7795c5b5ba2b9abca9af6cdb8fa6e');

INSERT INTO users (nome, cognome, email, telefono, password_hash_(sha256), password_hash_(sha512))
VALUES ('Lorenzo', 'Greggio', 'lorenzo.greggio@gmail.com', 393706824768, 'f23854bc9371d0c31e26753d1d13345632088784cd00acf715cd1a2b84280192', '70fc7a1f5fdf1fe18aab8fe050b7914207d3a96561a70e3877249ffe67a9e52d32fe1edd2aaff1c04b5af5cdd16e1931b0366956387f5cfadfcf187a5c7eba53');

INSERT INTO users (nome, cognome, email, telefono, password_hash_(sha256), password_hash_(sha512))
VALUES ('Vanessa', 'Fermi', 'vanessa.fermi@alice.it', 393507051180, '585db20b6df75716b2f9040ecddc1b3e34c922666859c82bea49a63a1575e20a', '9b9e8cb0218ec448792234f07d3d1410c29611f74474fc29c1c33d16be6f6a24a38f28c2186e96a12294e45f41f22fca42ec524cdf1864155e63f131708ca758');
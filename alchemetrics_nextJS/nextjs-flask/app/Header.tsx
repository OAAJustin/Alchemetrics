// components/Header.tsx
import React from 'react';
import Link from 'next/link';

const Header: React.FC = () => {
    return (
        <div style={{ position: 'fixed', width: '100%', background: '#fff', borderBottom: '1px solid #ccc', padding: '12.5px', margin: '-100px', color: 'black', fontSize: '27px'}}>
            <nav>
                <Link href="/">Home</Link> | <Link href="/Inventory">Inventory</Link> | <Link href="/archive">Archive</Link>
            </nav>
        </div>
    );
}

export default Header;
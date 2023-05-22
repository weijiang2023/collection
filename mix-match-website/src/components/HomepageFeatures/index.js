import React from 'react';
import clsx from 'clsx';
import styles from './styles.module.css';

const FeatureList = [
  {
    title: '潮流单品',
    Svg: require('@site/static/img/algmon.docusaurus.stability.2.svg').default,
    description: (
      <>
        独一无二
      </>
    ),
  },
  {
    title: '专人买手',
    Svg: require('@site/static/img/algmon.docusaurus.core.1.svg').default,
    description: (
      <>
        体贴入微
      </>
    ),
  },
  {
    title: '核心匹配',
    Svg: require('@site/static/img/algmon.docusaurus.fast.0.svg').default,
    description: (
      <>
        引领时尚
      </>
    ),
  },
];

function Feature({Svg, title, description}) {
  return (
    <div className={clsx('col col--4')}>
      <div className="text--center">
        <Svg className={styles.featureSvg} role="img" />
      </div>
      <div className="text--center padding-horiz--md">
        <h3>{title}</h3>
        <p>{description}</p>
      </div>
    </div>
  );
}

export default function HomepageFeatures() {
  return (
    <section className={styles.features}>
      <div className="container">
        <div className="row">
          {FeatureList.map((props, idx) => (
            <Feature key={idx} {...props} />
          ))}
        </div>
      </div>
    </section>
  );
}

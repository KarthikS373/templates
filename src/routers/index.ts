import { Router } from 'express';

import healthRouter from './health.route';

import { routeLogger } from '../configs/logger';
// import isAuth from '../middlewares/auth.middleware';

const router = Router();

// Logger
router.use(routeLogger);

// Routes
router.use('/health', healthRouter);

// Development only routes
if (process.env.NODE_ENV === 'development') {
  router.use('/dev');
}

export default router;
